from autogen.agentchat import AssistantAgent

def create_agents_from_personas(personas, llm_config, shared_event, task_type="chat_between_friends"):
    agents = []
    if task_type=="chat_between_friends":
        for persona in personas:
            system_msg = (
            f"You are {persona['name']}, a {persona['age']}-year-old from {persona['city']} who enjoys {persona['interests']}. "
            f"Your personality: {persona['personality']} "
            f"You and your friend will either talk about a previously attended event or plan for the event or just talk about the event in general. Event: {shared_event}. "
            f"Have a casual conversation about it. Stay in character, avoid repeating your name, and don't break the fourth wall."
        )
            agent = AssistantAgent(
                name=persona["name"],
                llm_config=llm_config,
                system_message=system_msg,
                human_input_mode="NEVER"
            )
            agents.append(agent)
        return agents
    else:
        raise(f"Invalid task type: {task_type}")

