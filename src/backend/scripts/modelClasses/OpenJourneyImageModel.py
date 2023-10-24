
from .BaseImageModel import BaseImageModel
from diffusers import (
    StableDiffusionPipeline,
    EulerDiscreteScheduler
)


class OpenJourneyImageModel(BaseImageModel):
    name = "prompthero/openjourney-v4"

    def __init__(self):
        self.generator = None

    def prepare(self):
        self.generator = StableDiffusionPipeline.from_pretrained("prompthero/openjourney-v4")
        #self.generator.scheduler = EulerDiscreteScheduler.from_config(self.generator.scheduler.config)



