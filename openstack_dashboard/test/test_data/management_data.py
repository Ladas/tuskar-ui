#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from openstack_dashboard.api.management import (
    Flavor, ResourceClass, Host,
    Rack, ResourceClassFlavor)

import openstack_dashboard.dashboards.infrastructure.models as dummymodels

from .utils import TestDataContainer


def data(TEST):
    # Flavors
    TEST.management_flavors = TestDataContainer()
    flavor_1 = Flavor(dummymodels.Flavor(
            id="aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            name='m1.tiny'))
    flavor_2 = Flavor(dummymodels.Flavor(
            id="bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            name='m1.massive'))
    TEST.management_flavors.add(flavor_1, flavor_2)

    # Resource Classes
    TEST.management_resource_classes = TestDataContainer()

    resource_class_1 = ResourceClass(dummymodels.ResourceClass(
        id="1",
        service_type="compute",
        name="rclass1"))

    resource_class_2 = ResourceClass(dummymodels.ResourceClass(
        id="2",
        service_type="compute",
        name="rclass2"))

    """
    # FIXME to make code below work, every @property has to have
    # setter defined in API model
    flavors = []
    all_flavors = []
    resources = []
    all_resources = []

    @resources.setter
    def resources(self, value):
        self._resources = value
    resource_class_1.resources = resources
    resource_class_2.resources = resources

    resource_class_1.all_resources = all_resources
    resource_class_2.all_resources = all_resources

    resource_class_1.flavors = flavors
    resource_class_2.flavors = flavors

    resource_class_1.all_flavors = all_flavors
    resource_class_2.all_flavors = all_flavors
    """

    TEST.management_resource_classes.add(resource_class_1, resource_class_2)

    #Racks
    TEST.management_racks = TestDataContainer()
    rack_1 = Rack(dummymodels.Rack(
        id="1",
        name='rack1',
        resource_class_id='1'))

    TEST.management_racks.add(rack_1)

    #ResourceClassFlavors
    TEST.management_resource_class_flavors = TestDataContainer()
    resource_class_flavor_1 = ResourceClassFlavor(
        dummymodels.ResourceClassFlavor(
            id="1",
            max_vms='16',
            resource_class_id=1,
            flavor_id=1))

    TEST.management_resource_class_flavors.add(resource_class_flavor_1)

    # Hosts
    TEST.hosts = TestDataContainer()
    TEST.unracked_hosts = TestDataContainer()

    host_1 = Host(dummymodels.Host(id="1",
                                   name="host1",
                                   rack_id=1,
                                   mac_address="00-B0-D0-86-AB-F7",
                                   ip_address="192.168.191.11",
                                   status="active",
                                   usage="20"))
    host_2 = Host(dummymodels.Host(id="2",
                                   name="host2",
                                   rack_id=1,
                                   mac_address="00-B0-D0-86-AB-F8",
                                   ip_address="192.168.191.12",
                                   status="active",
                                   usage="20"))
    host_3 = Host(dummymodels.Host(id="3",
                                   name="host3",
                                   rack_id=1,
                                   mac_address="00-B0-D0-86-AB-F9",
                                   ip_address="192.168.191.13",
                                   status="active",
                                   usage="20"))
    host_4 = Host(dummymodels.Host(id="4",
                                   name="host4",
                                   rack_id=1,
                                   mac_address="00-B0-D0-86-AB-F0",
                                   ip_address="192.168.191.14",
                                   status="active",
                                   usage="20"))
    host_5 = Host(dummymodels.Host(id="5",
                                   name="host5",
                                   mac_address="00-B0-D0-86-AB-F1"))

    TEST.hosts.add(host_1, host_2, host_3, host_4)
    TEST.unracked_hosts.add(host_5)
