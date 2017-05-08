# -*- coding:utf-8 -*-

from Tkinter import *
import random
import time

#小球部分
class Ball:
	def __init__(self,canvas,paddle,score,color):
		self.canvas = canvas
		self.paddle = paddle
		self.score = score
		self.id = canvas.create_oval(10,10,25,25,fill=color) #将图形ID的值赋给self.id
		self.canvas.move(self.id,245,100) #图形初始化所在位置
		starts = [-3,-2,-1,1,2,3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height() #winfo函数获取当前画布高度
		self.canvas_width = self.canvas.winfo_width() #winfo函数获取当前画布宽度
		self.hit_bottom = False
		
	def hit_paddle(self,pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if  pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				self.x += self.paddle.x
				self.score.hit()
				return True
		return False
	
	def draw(self):
		self.canvas.move(self.id,self.x,self.y) 
		pos = self.canvas.coords(self.id)  #coords函数返还左上角以及右下角坐标
		#是否撞墙
		if pos[1] <= 0:
			self.y = 1
		if pos[3] >= self.canvas_height:
			self.hit_bottom = True   #小球到底部停止
		# 撞拍改变方向
		if self.hit_paddle(pos) == True:
			self.y = -3
		if pos[0] <=0:
			self.x = 3
		if pos[2] >=self.canvas_width:
			self.x = -3

#球拍			
class Paddle:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0,0,100,10,fill=color)
		self.canvas.move(self.id,200,300)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.started = False
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
		self.canvas.bind_all('<Button-1>', self.start_game)
		
	def draw(self):
		self.canvas.move(self.id,self.x,0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		if pos[2] >= self.canvas_width:
			self.x = 0
	
	def turn_left(self,evt):
		self.x = -2
		
	def turn_right(self,evt):
		self.x = 2
	
	def start_game(self,evt):
		self.started = True

#分数统计
class Score:
	def __init__(self, canvas, color):
		self.score = 0
		self.canvas = canvas
		self.id = canvas.create_text(450, 10, text=self.score, fill=color)
		
	def hit(self):
		self.score += 1
		self.canvas.itemconfig(self.id,text=self.score)
	
tk = Tk()
tk.title("Game") #窗口命名
tk.resizable(0,0)  #窗口不可改变
tk.wm_attributes("-topmost", 1) #窗口置顶
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0) #后两个参数，确保画布之外没有边框
canvas.pack()
tk.update()

score = Score(canvas,'blue')
paddle = Paddle(canvas, 'green')
ball = Ball(canvas,paddle,score, 'red')
game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')

while 1:
	if ball.hit_bottom == False and paddle.started == True:   #没碰到底部，就继续游戏
		ball.draw()
		paddle.draw()
	if ball.hit_bottom == True:
		time.sleep(1)
		canvas.itemconfig(game_over_text,state='normal')
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)
