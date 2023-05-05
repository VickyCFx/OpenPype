# -*- coding: utf-8 -*-
"""Creator plugin for creating pointcache alembics."""
from openpype.hosts.max.api import plugin
from openpype.pipeline import CreatedInstance


class CreatePointCache(plugin.MaxCreator):
    identifier = "io.openpype.creators.max.pointcache"
    label = "Point Cache"
    family = "pointcache"
    icon = "gear"

    def create(self, subset_name, instance_data, pre_create_data):
        # from pymxs import runtime as rt

        instance = super(CreatePointCache, self).create(
            subset_name,
            instance_data,
            pre_create_data)  # type: CreatedInstance
        container = rt.getNodeByName(instance.data.get("instance_node"))
        # TODO: Disable "Add to Containers?" Panel
        # parent the selected cameras into the container
        sel_obj = None
        if self.selected_nodes:
            sel_obj = list(self.selected_nodes)
            for obj in sel_obj:
                obj.parent = container
        # for additional work on the node:
        # instance_node = rt.getNodeByName(instance.get("instance_node"))
