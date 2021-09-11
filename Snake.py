import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self,w,h):
        arcade.Sprite.__init__(self)
        self.color=arcade.color.RED
        self.width=16
        self.height=16
        self.center_x=random.randint(0, w)
        self.center_y=random.randint(0, h)
        self.r=8
        self.body=[]
        self.body.append([self.center_x,self.center_y])

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)
        for i in range(len(self.body)):
            arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

    def move(self):
        for i in range(len(self.body)):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][0] = self.body[i-1][1]

        self.center_x += self.speed * self. change_x
        self.center_y += self.speed * self. change_y

        if self.body:
            self.body[0][0] += self.speed *self.change_x
            self.body[0][1] += self.speed * self.change_y

    def eat(self,food):
        if food == "cactus":
            self.score -=1
            self.body.pop()
        elif food == "apple":
            self.score += 1
            print(self.body.append(self.body[len(self.body)+1]))
        elif food == "flower":
            self.body += 2
            print(self.body.append(self.body[len(self.body)+2]))        

class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color=arcade.color.BROWN
        self.speed = 8
        self.width=16
        self.height=16
        self.r=8
        self.score=0
        self.center_x = w // 2
        self.center_y = h // 2
        self.change_x=0
        self.change_y=0
       

    def draw(self):
        self.snake.draw()

    def move(self):
        self.center_x+= self.speed*self.change_x
        self.center_y+= self.speed*self.change_y

    def eat(self):
        self.score+=1

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,600,650,"snake")
        arcade.set_background_color(arcade.color.GRAY)
        self.snake=Snake(700,750) 
        self.apple=[]
        for i in range(10):
            self.apple.append(Apple(700,750))

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.flower):
            self.snake.eat("flower")
            self.flower = Flower(500,550)
            print(self.snake.score)
        elif arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat("apple")
            self.apple = Apple(500,550)
            print(self.snake.score)

        elif arcade.check_for_collision(self.snake, self.cactus):
            self.snake.eat("cactus")
            self.cactus = cactus(500,550)
            print(self.snake.score)

    def on_key_release(self,key,nodifiers):
        if key==arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0

        elif key==arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        
        elif key==arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1

        elif key==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1

        else:
            print("Button that pressure is not defined!")

class Flower(arcade.Sprite):
    def __init__(self,w,h):
            arcade.Sprite.__init__(self)
            self.color=arcade.color.PINK
            self.width=16
            self.height=16
            self.center_x=random.randint(0, w)
            self.center_y=random.randint(0, h)
            self.r=8
            self.body=[]
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class cactus(arcade.Sprite):   
    def __init__(self,w,h):
            arcade.Sprite.__init__(self)
            self.color=arcade.color.GREEN
            self.width=16
            self.height=16
            self.center_x=random.randint(0, w)
            self.center_y=random.randint(0, h)
            self.r=8
            self.body=[]
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)   

game=Game()
arcade.run()