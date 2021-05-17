from visual import *
import thread
import random
import math

class Fires:
    def __init__(self):
        self.ball = sphere(pos=(0,0,0), radius=0.05, color=vector(0,0,0), visible=False)
        self.dt = 0.01
        self.totaldt = 0
        self.fires = []#set small balls
        self.tail = []#set retain tails by small balls
        self.swi = False

    def __del__(self):
        print ("dell")

    def setColor(self,r,g,b):
        self.ball.color = vector(r,g,b)

    def rann(self):#0~2pi random number
        return random.random()*2*math.pi

    def funcInit(self,x,y,z,h,a,u):
        self.ball.pos = (x,y,z) #(x,y,z): balls position 
        self.ball.velocity = vector(0,h,0) #h: bigball yaxis velocity
        self.a = a #a: explosion speed of small balls 
        self.u = u #u: fireworks axis tilt angle

    def run_Twinkle(self,x,y,z,h,a,u): 
	self.funcInit(x,y,z,h,a,u)
        self.ball.visible=True

        while 1:
            rate(100)
            self.ball.pos = self.ball.pos + self.ball.velocity*self.dt
            self.ball.velocity.y = self.ball.velocity.y-10*self.dt

            #generating small balls, once original ball reached an apex
            if self.ball.velocity.y <= 0.5 and not self.swi:
                self.ball.visible = False
                for i in range(300) :
                    self.tt = self.rann()#theta
                    self.tp = self.rann()/2#pi
                    self.tx = 0.1*math.sin(self.tp)*math.cos(self.tt)
                    self.ty = 0.1*math.sin(self.tp)*math.sin(self.tt)
                    self.tz = 0.1*math.cos(self.tp)

                    self.fires.append(sphere(pos=(self.ball.x+self.tx, self.ball.y+self.ty, self.ball.z+self.tz),
                                             velocity=vector(self.tx*self.a, self.ty*self.a, self.tz*self.a),
                                             radius=0.02, color=self.ball.color, opacity=1))

                self.swi = True #explosion swich on.

            if self.swi:
                self.totaldt += self.dt*100
		opacity = 1.
                for i in range(300) :
                    self.fires[i].pos = self.fires[i].pos +self.fires[i].velocity*self.dt
                    self.fires[i].velocity.y = self.fires[i].velocity.y-0.5*self.dt
                    self.fires[i].opacity = self.fires[i].opacity-0.5*self.dt
                    randNum = random.randrange(0,2)
                    self.fires[i].color = (randNum, randNum, randNum)

            if self.totaldt == 300:
                break


    def run_Fire(self,x,y,z,h,a,u):
	self.funcInit(x,y,z,h,a,u)
        self.ball.visible=True

        while 1:
            rate(100)
            self.ball.pos = self.ball.pos + self.ball.velocity*self.dt
            self.ball.velocity.y = self.ball.velocity.y-10*self.dt

            #generating small balls, once original ball reached an apex
            if self.ball.velocity.y <= 0.5 and not self.swi:
                self.ball.visible = False
                for i in range(100):
                    self.tt = self.rann()#theta
                    self.tp = self.rann()/2#pi
                    self.tx = 0.1*math.sin(self.tp)*math.cos(self.tt)
                    self.ty = 0.1*math.sin(self.tp)*math.sin(self.tt)
                    self.tz = 0.1*math.cos(self.tp)

                    self.fires.append(sphere(pos=(self.ball.x+self.tx, self.ball.y+self.ty, self.ball.z+self.tz),
                                             velocity=vector(self.tx*self.a, self.ty*self.a, self.tz*self.a),
                                             radius=0.02, color=self.ball.color, opacity=1))
#                    self.tail.append(curve(pos=(self.ball.x+self.tx, self.ball.y+self.ty, self.ball.z+self.tz),
#                                           radius=0.01,color=self.ball.color))
                self.swi = True #explosion swich on.

            if self.swi:
                self.totaldt += self.dt*100
                for i in range(100):
                    self.fires[i].pos = self.fires[i].pos +self.fires[i].velocity*self.dt
                    self.fires[i].velocity.y = self.fires[i].velocity.y - 0.5 *self.dt
                    self.fires[i].opacity = self.fires[i].opacity-0.5*self.dt
#                    self.tail[i].append(pos=self.fires[i].pos, retain=40)
#                    self.tail[i].color = self.tail[i].color-(0.3*self.dt,0.3*self.dt,0.3*self.dt)
            if self.totaldt == 300:
                break

    def run_Circle(self,x,y,z,h,a,u):
	self.funcInit(x,y,z,h,a,u)
        self.ball.visible=True

        while 1:
            rate(100)
            self.ball.pos = self.ball.pos + self.ball.velocity*self.dt
            self.ball.velocity.y = self.ball.velocity.y-10*self.dt

            #generating small balls, once original ball reached an apex
            if self.ball.velocity.y <= 0.5 and not self.swi:
                self.ball.visible = False
                for i in range(100) :
                    self.tt = self.rann()#theta
                    self.tp = self.rann()/2#pi
                    self.tx = 0.1*math.cos(self.tt)
                    self.ty = 0.1*math.sin(self.tt+self.u)
                    self.tz = 0.1*math.cos(self.tt+0.5)

                    self.fires.append(sphere(pos=(self.ball.x+self.tx, self.ball.y+self.ty, self.ball.z+self.tz),
                                             velocity=vector(self.tx*self.a, self.ty*self.a, self.tz*self.a),
                                             radius=0.02, color=self.ball.color, opacity=1))

                self.swi = True #explosion swich on.

            if self.swi:
                self.totaldt += self.dt*100
                for i in range(100) :
                    self.fires[i].pos = self.fires[i].pos +self.fires[i].velocity*self.dt
                    self.fires[i].velocity.y = self.fires[i].velocity.y - 0.5 *self.dt
                    self.fires[i].opacity = self.fires[i].opacity-0.5*self.dt

            if self.totaldt == 300:
                break


    def run_8form(self,x,y,z,h,a,u):
	self.funcInit(x,y,z,h,a,u)
        self.ball.visible=True

        while 1:
            rate(100)
            self.ball.pos = self.ball.pos + self.ball.velocity*self.dt
            self.ball.velocity.y = self.ball.velocity.y-10*self.dt

            #generating small balls, once original ball reached an apex
            if self.ball.velocity.y <= 0.5 and not self.swi:
                self.ball.visible = False
                for i in range(100) :
                    self.tt = self.rann()#theta
                    self.tp = self.rann()/2#pi
                    self.tx = 0.1*math.sin(self.tt)*math.cos(self.tt)
                    self.ty = 0.1*math.cos(self.tt+self.u)
                    self.tz = 0.1*math.sin(self.tt)

                    self.fires.append(sphere(pos=(self.ball.x+self.tx, self.ball.y+self.ty, self.ball.z+self.tz),
                                             velocity=vector(self.tx*self.a, self.ty*self.a, self.tz*self.a),
                                             radius=0.02, color=self.ball.color, opacity=1))

                self.swi = True #explosion swich on.

            if self.swi == 1:
                self.totaldt += self.dt*100
                for i in range(100) :
                    self.fires[i].pos = self.fires[i].pos +self.fires[i].velocity*self.dt
                    self.fires[i].velocity.y = self.fires[i].velocity.y - 0.5 *self.dt
                    self.fires[i].opacity = self.fires[i].opacity-0.5*self.dt

            if self.totaldt == 300:
                break

