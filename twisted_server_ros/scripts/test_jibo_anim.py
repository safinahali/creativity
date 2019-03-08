#!/usr/bin/python


import rospy
from jibo_msgs.msg import JiboAction, JiboVec3, JiboAsrCommand
from std_msgs.msg import Header  # standard ROS msg header
import time
import json, sys


ROSCORE_TO_JIBO_TOPIC = '/jibo'


class RobotSender:

    def __init__(self):
        self.robot_commander = None
        self.robot_asr_commander = None

    def start_robot_publisher(self):
        """
        Starts up the robot publisher node
        """

        rospy.init_node('Jibo_Test_Node', anonymous=True)
        print('Robot Pub Node started')


        msgType = JiboAction
        msgTopic = ROSCORE_TO_JIBO_TOPIC

        self.robot_commander = rospy.Publisher(msgTopic, msgType, queue_size=10)
        self.robot_asr_commander = rospy.Publisher('jibo_asr_command', JiboAsrCommand, queue_size=1)
        rate = rospy.Rate(10)  # spin at 10 Hz
        rate.sleep()  # sleep to wait for subscribers


    def send_robot_motion_cmd(self, command):
        """
        send a Motion Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()


        msg.do_motion = True
        msg.do_tts = False
        msg.do_lookat = False

        msg.motion = command

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_tts_cmd(self, text, *args):
        """
        send a Motion Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()


        msg.do_motion = False
        msg.do_tts = True
        msg.do_lookat = False

        msg.tts_text = text

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_lookat_cmd(self, x, y, z):
        """
        send a Motion Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()


        msg.do_motion = False
        msg.do_tts = False
        msg.do_lookat = True

        position = JiboVec3(x, y, z)

        msg.look_at = position

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_audio_cmd(self, audio_command):
        """
        send a Motion Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()


        msg.do_motion = False
        msg.do_tts = False
        msg.do_lookat = False
        msg.do_sound_playback = True

        msg.audio_filename = audio_command

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_audio_motion_cmd(self, a, m):
        """
        send LED ring color Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()

        msg.do_sound_playback = True
        msg.do_motion = True

        msg.audio_filename = a
        msg.motion = m

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)


    def send_robot_led_cmd(self, r, g, b):
        """
        send LED ring color Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()

        msg.do_led = True

        color = JiboVec3(r, g, b)
        msg.led_color = color

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_volume_cmd(self, v):
        """
        send LED ring color Command to Jibo
        """

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()

        msg.do_volume = True

        msg.volume = v

        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_asr_cmd(self, cmd, heyjibo=False, continuous=False, rule=""):

        """
        send ASR Command to Jibo
        """

        msg = JiboAsrCommand()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()

        msg.heyjibo = heyjibo
        msg.continuous = continuous

        msg.rule = rule
        msg.command = cmd

        self.robot_asr_commander.publish(msg)
        rospy.loginfo(msg)

    def send_robot_anim_transition_cmd(self, tran):

        msg = JiboAction()
        # add header
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()

        msg.do_anim_transition = True
        msg.anim_transition = tran
        self.robot_commander.publish(msg)
        rospy.loginfo(msg)

def main(info):
    data = json.load(open(info[0]))

    new_rule = "TopRule = $* (love candy){%slotAction='world'%} | (love choco){%slotAction='mars'%} $*;"

    mySender = RobotSender()
    mySender.start_robot_publisher()
    mySender.send_robot_motion_cmd('reset.keys')

    mySender.send_robot_tts_cmd("")
    time.sleep(2)

    try:
        for condition in data[info[1]]:
            print data[info[1]][condition]
            for idx in data[info[1]][condition]:
                print idx
                tts_msg = idx[0].encode('ascii', 'ignore').replace('idle', '').split(':')[-1]
                print tts_msg
                mySender.send_robot_tts_cmd(tts_msg)
                time.sleep(2)
        exit()
    except TypeError:
        for idx in data[info[1]]:
            print idx
            tts_msg = idx[0].encode('ascii', 'ignore').replace('idle', '').split(':')[-1]
            mySender.send_robot_tts_cmd(tts_msg)
            time.sleep(2)
        exit()


    for item in data:

        try:
            for condition in data[item]:
                print data[item][condition]
                for idx in data[item][condition]:
                    print idx
                    tts_msg = idx[0].encode('ascii','ignore').replace('idle','').split(':')[-1]
                    print tts_msg
                    mySender.send_robot_tts_cmd(tts_msg)
                    time.sleep(len(tts_msg)*0.5)
        except:
            for idx in data[item]:
                print idx
                tts_msg = idx[0].encode('ascii','ignore').replace('idle','').split(':')[-1]
                mySender.send_robot_tts_cmd(tts_msg)
                time.sleep(len(tts_msg) * 0.5)


    rospy.spin()

if __name__ == '__main__':
    main(sys.argv[1:])
