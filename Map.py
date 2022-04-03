cylinderLink = """
<inertial>
  <mass>1</mass>
  <inertia>
    <ixx>0.145833</ixx>
    <ixy>0</ixy>
    <ixz>0</ixz>
    <iyy>0.145833</iyy>
    <iyz>0</iyz>
    <izz>0.125</izz>
  </inertia>
  <pose>0 0 0 0 -0 0</pose>
</inertial>
<pose>-1.5273 -1.35413 0 0 -0 0</pose>
<visual name='visual'>
  <pose>0 0 0 0 -0 0</pose>
  <geometry>
    <cylinder>
      <radius>0.5</radius>
      <length>1</length>
    </cylinder>
  </geometry>
  <material>
    <lighting>1</lighting>
    <script>
      <uri>file://media/materials/scripts/gazebo.material</uri>
      <name>Gazebo/Grey</name>
    </script>
    <shader type='pixel'/>
  </material>
  <transparency>0</transparency>
  <cast_shadows>1</cast_shadows>
</visual>
<collision name='collision'>
  <laser_retro>0</laser_retro>
  <max_contacts>10</max_contacts>
  <pose>0 0 0 0 -0 0</pose>
  <geometry>
    <cylinder>
      <radius>0.5</radius>
      <length>1</length>
    </cylinder>
  </geometry>
  <surface>
    <friction>
      <ode>
        <mu>1</mu>
        <mu2>1</mu2>
        <fdir1>0 0 0</fdir1>
        <slip1>0</slip1>
        <slip2>0</slip2>
      </ode>
      <torsional>
        <coefficient>1</coefficient>
        <patch_radius>0</patch_radius>
        <surface_radius>0</surface_radius>
        <use_patch_radius>1</use_patch_radius>
        <ode>
          <slip>0</slip>
        </ode>
      </torsional>
    </friction>
    <bounce>
      <restitution_coefficient>0</restitution_coefficient>
      <threshold>1e+06</threshold>
    </bounce>
    <contact>
      <collide_without_contact>0</collide_without_contact>
      <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
      <collide_bitmask>1</collide_bitmask>
      <ode>
        <soft_cfm>0</soft_cfm>
        <soft_erp>0.2</soft_erp>
        <kp>1e+13</kp>
        <kd>1</kd>
        <max_vel>0.01</max_vel>
        <min_depth>0</min_depth>
      </ode>
      <bullet>
        <split_impulse>1</split_impulse>
        <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
        <soft_cfm>0</soft_cfm>
        <soft_erp>0.2</soft_erp>
        <kp>1e+13</kp>
        <kd>1</kd>
      </bullet>
    </contact>
  </surface>
</collision>
<self_collide>0</self_collide>
<enable_wind>0</enable_wind>
<kinematic>0</kinematic>
</link>"""

cylinderLinkGazebo = """
  <velocity>0 0 0 0 -0 0</velocity>
  <acceleration>0 0 0 0 -0 0</acceleration>
  <wrench>0 0 0 0 -0 0</wrench>
</link>"""


class Map:
    def __init__(self, size, density):
        self.size = size
        self.density = density
        self.link_str = ""
        self.link_str2 = ""

    def writeLinks(self):

        idx = 0
        num = self.size // self.density + 1
        margin = (self.size - (num - 1) * self.density) / 2
        # print("margin")
        # print(margin)
        startX = float(0 - (self.size / 2) + margin)
        startY = float(self.size / 2 - margin)

        # print("num")
        # print(num)
        # print("start Y")

        # print(startY)
        # print("check")
        # print(0 - self.size / 2)
        while 1:
            if startX > self.size / 2 - margin:
                startX = float(0 - (self.size / 2) + margin)
                startY = startY - self.density

            if startY < 0 - self.size / 2 + margin:
                break

            if startX >= -0.5 and startX <= 0.5 and startY >= -0.5 and startY <= 0.5:
                startX = startX + self.density
                continue
            # print("idx" + str(idx))
            # print(startX)
            # print(startY)
            link_name = "<link name='link_" + str(idx) + "'>"
            # print(link_name)
            self.link_str = self.link_str + "\n" + link_name + cylinderLink
            pose_str = "  <pose>" + str(startX) + " " + str(startY) + " 0.5 0 -0 0</pose>"
            self.link_str2 = self.link_str2 + "\n" + link_name + pose_str + cylinderLinkGazebo
            startX = startX + self.density

            idx = idx + 1

        # print(self.link_str)
        # print(self.link_str2)

    def drawmap(self):
        f = open("src/Anton_description/world/modelTest.sdf", "w+")

        tmpFile = (
            """<sdf version='1.7'>
  <world name='default'>
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
      <spot>
        <inner_angle>0</inner_angle>
        <outer_angle>0</outer_angle>
        <falloff>0</falloff>
      </spot>
    </light>
    <model name='ground_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <contact>
              <collide_bitmask>65535</collide_bitmask>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
    <gravity>0 0 -9.8</gravity>
    <magnetic_field>6e-06 2.3e-05 -4.2e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
    <physics type='ode'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <wind/>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
    <model name='7x7'>
      <pose>0 0 0 0 -0 0</pose>
      <link name='Wall_5'>
        <collision name='Wall_5_Collision'>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_5_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>-3.73884 -0.023751 0 0 -0 -1.5615</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_6'>
        <collision name='Wall_6_Collision'>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_6_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>0.043709 -3.79603 0 0 -0 0.007033</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_7'>
        <collision name='Wall_7_Collision'>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_7_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>3.73007 0.017405 0 0 -0 1.58229</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_8'>
        <collision name='Wall_8_Collision'>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_8_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>"""
            + str(self.size)
            + """ 0.15 1.0</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>-0.043741 3.76344 0 0 -0 -3.13056</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <static>1</static>
    </model>
    <model name='5obstacles'>
      """
            + self.link_str
            + """
      <static>0</static>
      <allow_auto_disable>1</allow_auto_disable>
      <pose>-1.56552 1.02499 0.5 0 -0 0</pose>
    </model>
    <state world_name='default'>
      <sim_time>139 111000000</sim_time>
      <real_time>149 958127173</real_time>
      <wall_time>1647481989 587860615</wall_time>
      <iterations>139111</iterations>
      <model name='5obstacles'>
        <pose>0 0 0 0.5 0 -0 0</pose>
        <scale>1 1 1</scale>
        """
            + self.link_str2
            + """
      </model>
      <model name='7x7'>
        <pose>0 0 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='Wall_5'>
          <pose>-"""
            + str(self.size / 2)
            + """ 0 -0.75 0 0 -1.57</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_6'>Wall
          <pose>0 -"""
            + str(self.size / 2)
            + """ -0.75 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_7'>
          <pose>"""
            + str(self.size / 2)
            + """ 0 -0.75 0 -0 1.57</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_8'>
          <pose>0 """
            + str(self.size / 2)
            + """ -0.75 0 0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='ground_plane'>
        <pose>0 0 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose>0 0 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <light name='sun'>
        <pose>0 0 10 0 -0 0</pose>
      </light>
    </state>
    <gui fullscreen='0'>
      <camera name='user_camera'>
        <pose>0 0 20 -1.2e-05 1.5698 1.54017</pose>
        <view_controller>orbit</view_controller>
        <projection_type>perspective</projection_type>
      </camera>
    </gui>
  </world>
</sdf>"""
        )

        f.write(tmpFile)
        f.close()


from curses.ascii import isdigit
from tkinter import *

root = Tk()


def buildMap():
    val1 = field1.get()
    val2 = field2.get()
    errorLabel.config(text="")
    successLabel.config(text="")
    if val1 == "" or val2 == "":
        errorLabel.config(text="Invalid value(s)")
        return

    for i in range(0, len(val1)):
        if not isdigit(val1[i]):
            errorLabel.config(text="Enter a valid value for the size of the map")
            field1.delete(0, END)
            return

    for i in range(0, len(val2)):
        if not isdigit(val2[i]):
            errorLabel.config(text="Please valid value for distance between obstacles")
            field2.delete(0, END)
            return

    print(val1)
    print(val2)

    field1.delete(0, END)
    field2.delete(0, END)

    size = val1
    desity = val2
    map = Map(float(size), float(desity))
    print("a " + str(size) + " by " + size + " map with desity " + desity + " is created")
    successLabel.config(
        text="Map configuration successful!\n"
        + "Size: "
        + size
        + " by "
        + size
        + "\n"
        + "Distance between obstacles: "
        + desity
    )

    map.writeLinks()
    map.drawmap()
    buttonSub.pack_forget()
    buttonClose.pack()


root.geometry("400x350")
frame = Frame(root)
frame.pack()

label1 = Label(frame, text="Enter the size of map (in meters)")
label1.pack(padx=10, pady=4)

field1 = Entry(frame, text="")
field1.pack(padx=10, pady=4)

# font size
label2 = Label(frame, text="Enter the distance between obstacles (in meters)")
label2.pack(padx=10, pady=4)

field2 = Entry(frame, text="")
field2.pack(padx=10, pady=4)

successLabel = Label(frame, text="", fg="green")
successLabel.pack()

errorLabel = Label(frame, text="", fg="red")
errorLabel.pack()

buttonSub = Button(frame, text="Submit", command=buildMap)
buttonSub.pack()

buttonClose = Button(frame, text="Close", command=root.destroy)


root.title("Map customization")
root.mainloop()
