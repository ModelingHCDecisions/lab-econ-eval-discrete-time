import MarkovModelClasses as Cls
import SimPy.SamplePathClasses as PathCls
import SimPy.FigureSupport as Fig
import InputData as D
import ParameterClasses as P
import Support as Support

# create a cohort
myCohort = Cls.Cohort(id=1,
                      pop_size=D.POP_SIZE,
                      parameters=P.ParametersFixed(therapy=P.Therapies.MONO))

# simulate the cohort over the specified time steps
myCohort.simulate(n_time_steps=D.SIM_TIME_STEPS)

# plot the sample path (survival curve)
PathCls.graph_sample_path(
    sample_path=myCohort.cohortOutcomes.nLivingPatients,
    title='Survival Curve',
    x_label='Time-Step (Year)',
    y_label='Number Survived')

# plot the histogram of survival times
Fig.graph_histogram(
    data=myCohort.cohortOutcomes.survivalTimes,
    title='Histogram of Patient Survival Time',
    x_label='Survival Time (Year)',
    y_label='Count',
    bin_width=1)

# print the outcomes of this simulated cohort
Support.print_outcomes(myCohort.cohortOutcomes, 'Mono therapy:')