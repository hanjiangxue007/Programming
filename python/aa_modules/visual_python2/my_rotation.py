from __future__ import division
from __future__ import print_function
from visual import *
from time import sleep
from commands import *

def GetScreenShot(FrameNumber):         # Take a screenshot and write
                                        # it to a numbered file.
    tmp = getoutput('/usr/sbin/screencapture celestial_sphere.%03d.pdf' % FrameNumber)
    print('Frame: %d' % (FrameNumber))
    return


scene.width=500
scene.height=500

R=10.0
thick=R/100
tilt=23.45#23.45 #degrees

earth=sphere(radius=1,color=color.blue)
ceq=ring(radius=R, axis=(0,1,0), thickness=thick, color=color.cyan)
caxis=cylinder(radius=thick, pos=(0,-R/4,0), axis=(0,R/2,0), color=color.white)
ecliptic=ring(radius=R, axis=(0,1,0), thickness=thick, color=color.yellow)
#tilt the ecliptic
ecliptic.axis=rotate(ecliptic.axis, angle=-pi/180*tilt)
sun=sphere(radius=1.0/2, color=color.yellow, pos=(0,0,R))
season = label(pos=(0,1.2*R,0), text='Season', xoffset=0, yoffset=0, space=0, height=20, border=10)
# day_label = label(pos=(0,-1.2*R,0), text='Day 1', xoffset=0, yoffset=0, space=0, height=20, border=10)
# northern_hem = label(pos=(-R,R,0), text="Northern Hemisphere", xoffset=0, yoffset=0, space=0, height=20, border=10)
# southern_hem = label(pos=(-R,-R,0), text="Southern Hemisphere", xoffset=0, yoffset=0, space=0, height=20, border=10)

scene.autoscale=0
scene.forward=rotate(vector(0,0,-1), angle=5*pi/180,axis=(0,1,0))

theta=0 #initial theta
dtheta=360/365*pi/180 #theta step
tol=dtheta/2 #tolerance

rotationrate=1
maxcameraangle=15
cameraangle=0
FrameNumber=1

while cameraangle<maxcameraangle:
    rate(10)
    cameraangle=cameraangle+rotationrate
    scene.forward=rotate(scene.forward, angle=-rotationrate*pi/180,axis=(1,0,0))

# **movie** By positioning the VPython window in the top left hand corner, we
# know its position on the screen and then can correctly crop it out
# of the screenshot afterwards.
#
print('This program works only on MacOSX but could be extended to Unix/Linux.')
print('This program does NOT work on Microsoft Windows.')
raw_input('Position VPython window at top left hand corner. Then hit enter in this window.')
#

while theta<361*pi/180:
    rate(10)

    cycles=int(theta/2/pi)+1e-10
    phi=theta-(2*pi)*cycles

    if((phi>0-tol and phi<tol) or phi>2*pi-tol):
        season.text="Autumnal Equinox (~ Sept. 22)"
        sleep(3)
#       scene.mouse.getclick()
    elif(phi>(pi/2-tol) and phi<(pi/2+tol)):
        season.text="Winter Solstice (~ Dec. 21)"
        sleep(3)
#       scene.mouse.getclick()
    elif(phi>(pi-tol) and phi<(pi+tol)):
        season.text="Vernal Equinox (~ Mar. 20)"
        sleep(3)
#       scene.mouse.getclick()
    elif(phi>(3*pi/2-tol) and phi<(3*pi/2+tol)):
        season.text="Summer Solstice (~ June 21)"
        sleep(3)
#       scene.mouse.getclick()
    else:
        season.text=""

    sun.pos.x=R*sin(theta)*cos(tilt*pi/180)
    sun.pos.z=R*cos(theta)
    sun.pos.y=-R*sin(theta)*sin(tilt*pi/180)

#   day=int(phi*180/pi*365/360+1)+1.
#   day_text="Day day" + day
#   day_label.text=day_text

    theta=theta+dtheta

## **movie** Use the screencapture utility to get a screenshot.
    #GetScreenShot(FrameNumber)
    #FrameNumber = FrameNumber + 1
##
