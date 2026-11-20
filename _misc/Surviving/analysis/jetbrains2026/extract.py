import csv,sys
csv.field_size_limit(10**9)
G="""response_id weight employment_status job_role position_level code_yrs age_range country company_size company_sizeM region3 region4 project_types
workusage_ai_coding usage_ai_coding mostused_ai_coding workusage_ai_coding_imputed_final usage_ai_coding_imputed_final mostused_ai_coding_imputed_final trial_ai_coding_imputed_final
types_ai_assistance_frequency percentage_code_generated_by expect_ai_to_write_more_less_code emotions_about_ai_society stop_factors_agents_workuse ai_benefits ai_paying_tools ai_tools_additional_credits team_use_remoteagents perecentage_work_tasks_done_agents quality_solutions_by_agents_compared_to_people actions_when_dissat_agents_output review_code_agents_frequency what_review_code_generate_agents percentage_agents_code_rewrite effort_review_agents_pr_vs_colleague full_permision_mode_agents_frequency agents_simultaneously_run agents_run_time practices_agents_coding
security_AI_effect_company security_AI_effect security_AI_trust security_AI_review security_AI_review_AI security_AI_compare security_AI_risk security_AI_help
question__633 question__635 ai_purchasing_company_policy question__504 question__505 ai_coding_tasks_freq ai_coding_delegate concerns_ai_coding ai_coding_statements_future types_ai_assistance_enjoy dx_technical_debt
dx_roi_satisfaction dx_roi_observed_from_ai company_ai_spendings_expectations company_ai_spendings_concern company_ai_spending_optimizations dx_ai_effect_on_productivity dx_dev_changes dx_remote_agents_risk dx_ai_feeling_dx dx_sense_code_ownership_after_ai dx_sense_control_after_ai question__1658 question__1657 dx_perc_on_activities_involving_code dx_ai_introduced job_challenges job_layoffs_experience dx_ai_layoffs job_security_feeling job_market_conditions job_change job_career_choice study_it question__964 question__967 question__968 question__936 question__1585 ai_affect_skills ai_mental_workload selfmon_problems selfmon_burnout_experience ai_time_saving percentage_code_generated_by_sum_for_filtering suspected_salary""".split()
G=set(G)
with open(sys.argv[1],newline='',encoding='utf-8') as f, open(sys.argv[2],'w',newline='',encoding='utf-8') as o:
    r=csv.reader(f); h=next(r)
    keep=[i for i,c in enumerate(h) if c.split('::')[0] in G]
    w=csv.writer(o); w.writerow([h[i] for i in keep]); n=0
    for row in r:
        w.writerow([row[i] for i in keep]); n+=1
print(n,len(keep))
