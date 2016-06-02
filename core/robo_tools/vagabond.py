#!/usr/bin/env python

import logging

from cops_and_robots.robo_tools.robot import Robot
from cops_and_robots.robo_tools.planner import MissionPlanner

class Vagabond(Robot):
    """The Vagabond subclass of the generic Robot type.
    Parameters
    ----------
    name : str
        The robot's name.
    **kwargs
        Arguments passed to the ``Vagabond`` superclass.
    Attributes
    ----------
    mission_statuses : {'on the run'}
    """
    mission_planner_defaults = {}
    goal_planner_defaults = {'type_': 'simple',
                             'use_target_as_goal': True}
    path_planner_defaults = {'type_': 'direct'}

    def __init__(self,
                 name,
                 pose=None,
                 pose_source='python',
                 map_cfg={},
                 mission_planner_cfg={},
                 goal_planner_cfg={},
                 path_planner_cfg={},
                 **kwargs):
        # Use class defaults for kwargs not included
        mp_cfg = Vagabond.mission_planner_defaults.copy()
        mp_cfg.update(mission_planner_cfg)
        gp_cfg = Vagabond.goal_planner_defaults.copy()
        gp_cfg.update(goal_planner_cfg)
        pp_cfg = Vagabond.path_planner_defaults.copy()
        pp_cfg.update(path_planner_cfg)
        super(Vagabond, self).__init__(name,
                                     pose=pose,
                                     pose_source=pose_source,
                                     goal_planner_cfg=gp_cfg,
                                     path_planner_cfg=pp_cfg,
                                     map_cfg=map_cfg,
                                     create_mission_planner=False,
                                     color_str='red',
                                     **kwargs)

        self.found_vagabond = {}
        self.mission_planner = RobberMissionPlanner(self, **mp_cfg)


class VagabondMissionPlanner(MissionPlanner):
    # """The Cop subclass of the generic MissionPlanner
    # """
    # mission_statuses = ['on the run', 'captured']

    def __init__(self, robot, mission_status='on the run'):

        super(VagabondMissionPlanner, self).__init__(robot,
                                                   mission_status=mission_status)

    def update(self):
        """Update the robot's status
        """
        self.mission_status = 'on the run'
        # Does not make sence anymore but still needs the update
        # if self.robot.name in self.robot.found_vagabond.keys():
        #     self.mission_status = 'on the run'
        # if self.mission_status is 'on the run':
        #     self.stop_all_movement()
