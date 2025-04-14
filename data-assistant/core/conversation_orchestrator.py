from autogen.agentchat import GroupChat, AssistantAgent

def run_conversation(agents, max_rounds=6):
    print("Agents received:", [a.name for a in agents])

    groupchat = GroupChat(
        agents=agents,
        messages=[],
        speaker_selection_method="round_robin"
    )
    print("GroupChat created")

    first_agent = agents[0]
    second_agent = agents[1]

    init_msg = {
        "role": "assistant",
        "name": first_agent.name,
        "content": f"Hey {second_agent.name}! It's been a while. What have you been up to?"
    }
    groupchat.append(init_msg, speaker=first_agent)

    print("Initial message appended\n💬 Starting manual conversation...\n")

    last_speaker = first_agent

    for i in range(max_rounds):
        turn_num = i + 1
        speaker = groupchat.select_speaker(last_speaker=last_speaker, selector=None)

        # Dynamically inject turn awareness
        turn_hint = {
            "role": "system",
            "name": "TurnManager",
            "content": f"This is turn {turn_num} of {max_rounds}. Please continue the conversation naturally."
        }
        groupchat.append(turn_hint, speaker=speaker)

        reply_msg = speaker.generate_reply(groupchat.messages)

        message = {
            "role": "assistant",
            "name": speaker.name,
            "content": reply_msg
        }

        groupchat.append(message, speaker=speaker)
        print(f"[{speaker.name}]: {reply_msg}")
        last_speaker = speaker
    return groupchat.messages

