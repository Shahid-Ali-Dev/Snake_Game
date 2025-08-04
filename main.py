from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score
score = Score()
s = Screen()
s.screensize(600,600)
s.bgcolor("coral")
s.title("poop eater")
s.tracer(0)
snake = Snake()
food = Food()

snake.create_snake()
s.update()
s.listen()

while snake.game_over:
    time.sleep(0.06)
    s.update()
    score.display()
    snake.move()
    if snake.first.distance(food) < 15:

        snake.extra()
        score.score()
        food.refresh()
        score.clear()

    if snake.first.xcor() >= 382 or snake.first.xcor() <= -382 or snake.first.ycor() >= 340 or snake.first.ycor() <= -340:
        snake.game_over = False

    for sn in range(len(snake.lst)):
        if snake.first.distance(snake.lst[sn]) <= 10 and sn != 0:
            snake.game_over = False

    for l in snake.lst:
            s.onkey(snake.le, "Left")
            s.onkey(snake.r, "Right")
            s.onkey(snake.u, "Up")
            s.onkey(snake.d, "Down")


score.over()
s.exitonclick()