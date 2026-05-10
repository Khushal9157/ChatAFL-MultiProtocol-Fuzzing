"""
State-Aware Dynamic Prompting Extension for ChatAFL

This implementation extends ChatAFL by introducing
state-aware prompt generation for protocol fuzzing.

The prompt generation dynamically adapts according to:
- current protocol state
- server responses
- previously explored states
- coverage feedback
"""

class StateAwarePromptGenerator:

    def __init__(self):
        self.visited_states = set()
        self.response_history = []
        self.coverage_history = []

    def update_state(self, protocol_state):
        self.visited_states.add(protocol_state)

    def add_response(self, response):
        self.response_history.append(response)

    def add_coverage(self, coverage):
        self.coverage_history.append(coverage)

    def generate_prompt(self,
                        protocol,
                        current_state,
                        previous_message,
                        server_response):

        state_context = f"""
Protocol: {protocol}

Current State:
{current_state}

Previous Message:
{previous_message}

Server Response:
{server_response}

Previously Explored States:
{list(self.visited_states)}

Coverage Feedback:
{self.coverage_history[-5:]}
"""

        adaptive_instruction = """
Generate the next protocol message while:
- exploring unexplored protocol states
- avoiding repetitive transitions
- maximizing protocol coverage
- maintaining semantic correctness
"""

        final_prompt = state_context + adaptive_instruction

        return final_prompt


# Example usage

if __name__ == "__main__":

    generator = StateAwarePromptGenerator()

    generator.update_state("RTSP_SETUP")
    generator.update_state("RTSP_PLAY")

    generator.add_response("200 OK")
    generator.add_coverage("7.42%")

    prompt = generator.generate_prompt(
        protocol="RTSP",
        current_state="RTSP_PLAY",
        previous_message="PLAY rtsp://example.com/video",
        server_response="200 OK"
    )

    print(prompt)