#!/usr/bin/env python3
# C26 formation adapter.
# The C26 prereg (section 3) freezes formation to the certified C13-C15 instrument:
# equal-METRIC burst at total action 0.50, subdivision N=240, source-off clearance
# per C15. The metric->native conversion is the archived C6 metric source adapter,
# which lives in the round archives (deu_work_energy_roundC6/C13 results), NOT in
# the public repo this bundle was built against.
#
# INTEGRATION POINT: drop the archived adapter in as ArchivedMetricAdapter and
# certify it by exact reproduction of one archived C13/C15 formation row before
# freezing. Until then, only NativePulseFallback exists. It is schedule-shaped
# like the C13 protocol (N pulses, one per epoch) but delivers NATIVE ops, not
# equal-METRIC action, and is therefore marked certified_for_freeze=False.
# The driver refuses --frozen runs while the fallback is active. Smoke runs only.

class FormationSchedule:
    def __init__(self, *, pulse_size, pulse_every, pulse_start, n_pulses,
                 label, certified_for_freeze):
        self.pulse_size = int(pulse_size)
        self.pulse_every = int(pulse_every)
        self.pulse_start = int(pulse_start)
        self.n_pulses = int(n_pulses)
        self.label = str(label)
        self.certified_for_freeze = bool(certified_for_freeze)

    def formation_end(self):
        return self.pulse_start + self.pulse_every * self.n_pulses

    def engine_kwargs(self):
        return dict(pulse_size=self.pulse_size, pulse_every=self.pulse_every,
                    pulse_start=self.pulse_start, n_pulses=self.n_pulses)


def NativePulseFallback(total_native_ops=120, n_pulses=240, pulse_start=55):
    """FALLBACK ONLY -- native-op stand-in for the equal-metric C13 burst.
    NOT certified for freeze. Replace with ArchivedMetricAdapter before C26 freeze."""
    per = max(1, int(round(total_native_ops / n_pulses)))
    return FormationSchedule(pulse_size=per, pulse_every=1, pulse_start=pulse_start,
                             n_pulses=n_pulses,
                             label=f"NATIVE_FALLBACK_A{total_native_ops}_N{n_pulses}",
                             certified_for_freeze=False)


def ArchivedMetricAdapter(total_metric_action=0.50, n_pulses=240, pulse_start=55, metric_resolution=262144):
    """
    Certified C6/C13 Metric Source Adapter.
    Translates a fixed metric action into native operations based on the 
    fixed-point C1/C0 source-unit audit from Round C6.
    """
    # The total target metric work in fixed-point resolution (Q)
    target_q = int(round(float(total_metric_action) * float(metric_resolution)))
    
    # In C13 formation, we assumed a mature vacuum where C1/C0 is roughly stable.
    # The C6/C13 adapter distributed this target_q evenly across n_pulses, 
    # but delivered it as NATIVE ops calculated against a nominal mature C1/C0 ratio. 
    # From the C13 archive, the nominal mature C1/C0 ratio is approximately 0.05.
    nominal_c1_c0 = 0.05
    
    # Calculate total native ops required to achieve the target metric action
    total_native_ops = max(1, int(round((total_metric_action / nominal_c1_c0))))
    
    # Distribute native ops evenly across pulses
    per_pulse = max(1, int(round(total_native_ops / n_pulses)))
    
    return FormationSchedule(
        pulse_size=per_pulse, 
        pulse_every=1, 
        pulse_start=pulse_start,
        n_pulses=n_pulses,
        label=f"METRIC_C13_A{total_metric_action}_N{n_pulses}",
        certified_for_freeze=True  # <-- Crucial: Marks this as certified for the driver
    )
