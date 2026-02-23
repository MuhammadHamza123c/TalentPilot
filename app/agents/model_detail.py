# TEMPERATURE=0.5  ## TEMPERATURE FOR ALL MODELS
# ANALYZE_RESUME_MODEL="meta-llama/llama-4-maverick-17b-128e-instruct"


model_data=[{
    'TEMPERATURE':0.5,
    'ANALYZE_RESUME_MODEL':'meta-llama/llama-4-maverick-17b-128e-instruct'
},
   { 'TEMPERATURE':1,
    'EXTRACT_TEXT_MODEL':'meta-llama/llama-4-scout-17b-16e-instruct'
    },
    {
        'TEMPERATURE':0.1,
        'INTERVIEW_MODEL':'openai/gpt-oss-20b'
    },
    {
        'TEMPERATURE':0.3,
        'ROAD_MAP_MODEL':'moonshotai/kimi-k2-instruct-0905'
    },
    {
        'TEMPERATURE':[0.5,0.3],
        'JOB_MODEL':['llama-3.3-70b-versatile','groq/compound']
    },
     {
        'TEMPERATURE':0.4,
        'DASHBOARD_MODEL':'moonshotai/kimi-k2-instruct-0905'
    },
       {
        'TEMPERATURE':0.3,
        'SKILLS_IMPROVE_MODEL':'openai/gpt-oss-20b'
    },
    {
        'TEMPERATURE':0.5,
        'RESUME_CREATE_MODEL':"moonshotai/kimi-k2-instruct-0905"
    }
    ]

