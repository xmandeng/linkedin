from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load your config
config_list = config_list_from_json("OAI_CONFIG_LIST")

# Create an AssistantAgent instance
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "model": "gpt-3.5-turbo",  # Adjust this to your specific Claude 3.5 model
    },
)

# Create a UserProxyAgent instance
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    },
)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="Let's create a web scraper for LinkedIn job postings in Legal Compliance.",
)
