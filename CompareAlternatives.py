import Support as Support
import econ_eval_hiv_model.input_data as data
import econ_eval_hiv_model.model_classes as model
import econ_eval_hiv_model.param_classes as param

# simulating mono therapy
# create a cohort
cohort_mono = model.Cohort(id=0,
                           pop_size=data.POP_SIZE,
                           parameters=param.Parameters(therapy=param.Therapies.MONO))
# simulate the cohort
cohort_mono.simulate(n_time_steps=data.SIM_TIME_STEPS)

# simulating combination therapy
# create a cohort
cohort_combo = model.Cohort(id=1,
                            pop_size=data.POP_SIZE,
                            parameters=param.Parameters(therapy=param.Therapies.COMBO))
# simulate the cohort
cohort_combo.simulate(n_time_steps=data.SIM_TIME_STEPS)

# print the estimates for the mean survival time and mean time to AIDS
Support.print_outcomes(sim_outcomes=cohort_mono.cohortOutcomes,
                       therapy_name=param.Therapies.MONO)
Support.print_outcomes(sim_outcomes=cohort_combo.cohortOutcomes,
                       therapy_name=param.Therapies.COMBO)

# plot survival curves and histograms
Support.plot_survival_curves_and_histograms(sim_outcomes_mono=cohort_mono.cohortOutcomes,
                                            sim_outcomes_combo=cohort_combo.cohortOutcomes)


# print comparative outcomes
Support.print_comparative_outcomes(sim_outcomes_mono=cohort_mono.cohortOutcomes,
                                   sim_outcomes_combo=cohort_combo.cohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(sim_outcomes_mono=cohort_mono.cohortOutcomes,
                       sim_outcomes_combo=cohort_combo.cohortOutcomes)
