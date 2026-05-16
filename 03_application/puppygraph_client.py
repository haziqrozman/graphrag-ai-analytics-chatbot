"""
===========================================================================================
Script  : puppygraph_client.py
Purpose : Initialises the PuppyGraph client connection using the local host configuration.
===========================================================================================
"""

from puppygraph import PuppyGraphClient, PuppyGraphHostConfig

client = PuppyGraphClient(
    PuppyGraphHostConfig(
        ip="localhost", username="puppygraph", password="puppygraph123"
    )
)