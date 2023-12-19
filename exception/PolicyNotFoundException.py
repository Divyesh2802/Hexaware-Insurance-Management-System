class PolicyNotFoundException(Exception):
    def __init__(self, policy_id):
        super().__init__(f"Policy ID: {policy_id} not found in the system.")
