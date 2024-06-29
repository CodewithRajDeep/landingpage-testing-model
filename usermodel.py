from pyab import Experiment


# User model (replace with your actual user model)
class User:
  def __init__(self, id, email):
    self.id = id
    self.email = email

# Define the A/B experiment
experiment = Experiment("profile_picture_upload")
experiment.add_variation("control")  # Control group
experiment.add_variation("variation")  # Variation group with persuasive elements
experiment.allocate("control", 0.5)  # Allocate 50% traffic to control
experiment.allocate("variation", 0.5)  # Allocate 50% traffic to variation
