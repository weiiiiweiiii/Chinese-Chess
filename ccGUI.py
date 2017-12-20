#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:59:15 2017

@author: Yuliangze
"""



import tkinter as tk
from PIL import Image, ImageTk
import Model
import Control



class GameBoard():

    def __init__(self):
        
        #Game on board
        self.Game = Model.ChessGame(Control.initialBoard())
        
        #load picture
        self.bgImage = Image.open('newBoard.png')
        
        #open up an window
        self.window = tk.Tk()

        #New Game
        self.newGameButton = tk.Button(master = self.window,
                text = '开启新的棋局（Start a New Game）',
                font = ('Helvetica',20))
        self.newGameButton.grid(row = 0, column = 0,sticky = tk.N + tk.S + tk.E + tk.W)
        
        #Quit Button
        self.quitButton = tk.Button(master = self.window,
                text = '退出（Quit）',
                font = ('Helvetica',20),command = self.quitGame)
        self.quitButton.grid(row = 1, column = 0,sticky = tk.N + tk.S + tk.E + tk.W)
        
        #Game Type
        self.gameLable = tk.Label(master = self.window,
                text = '中国象棋（Chinese Chess)',
                font = ('Helvetica',20))
        self.gameLable.grid(row = 2, column = 0,sticky = tk.W)
        
        #Turn Label
        self.turnLabel = tk.Label(master = self.window,
                text = f'玩家(Player): Red',
                font = ('Helvetica',20))
        self.turnLabel.grid(row = 3, column = 0, sticky = tk.W)

        #Show Winner Label
        self.winnerLabel = tk.Label(master = self.window,
                text = '胜者(Winner): Have Not Been Decided Yet',
                font = ('Helvetica',20))
        self.winnerLabel.grid(row = 4, column = 0, sticky = tk.W)
        
        #create canvas
        self.canvas = tk.Canvas(self.window,width = 670,height = 670, highlightthickness=0)
        self.canvas.grid(row=5,padx = 15, pady = 15, sticky=tk.W+tk.E+tk.N+tk.S)
        
        #stretch the game board
        self.window.rowconfigure(5, weight = 1)
        self.window.columnconfigure(0, weight = 1)
        
        
        #widght to resize window
        self.window.bind("<Configure>", self.resizeHandler)
        #widght to click on canvas
        self.canvas.bind('<Button-1>',self.clickedHandler)

        
    
    def resizeHandler(self,event):
        '''
            resize everything on canvas
        '''
        canvasWidth = self.canvas.winfo_width()
        canvasHeight = self.canvas.winfo_height()
        
        self.canvas.delete(tk.ALL)

        self._drawBoard(canvasWidth,canvasHeight)
        self._drawChess(canvasWidth,canvasHeight)
        
        
    def clickedHandler(self,event):
        '''
            click on canvas
        '''
        clickedX,clickedY = Control.getPoint(event)
        print(clickedX,clickedY,self.canvas.winfo_width(),self.canvas.winfo_height())
        
    def _drawBoard(self,canvasWidth,canvasHeight):
        '''
            draw game board
        '''
        size = (canvasWidth,canvasHeight)
        resized = self.bgImage.resize(size,Image.ANTIALIAS)
        self.currentBgImage = ImageTk.PhotoImage(resized)
        self.canvas.create_image(0, 0, image=self.currentBgImage, anchor=tk.NW)
        

    def _drawChess(self,canvasWidth,canvasHeight):
        '''
            canvasResize helper function
        '''
        radius = Model.CHESS_RADIUS
        for rows in self.Game:
            for point in rows:
                if point.content[0] != None :
                    x = point.fx
                    y = point.fy
                    color = lambda typeName: 'black' if typeName == 'b' else 'red'
                    self.canvas.create_oval(canvasWidth*(x-radius), 
                                            canvasHeight*(y-radius),
                                            canvasWidth*(x+radius),
                                            canvasHeight*(y+radius),
                                            fill = 'white',
                                            outline = 'black')
                    self.canvas.create_text(canvasWidth*x,
                                            canvasHeight*y,
                                            text=f'{str(point.content[0])}',
                                            fill = f'{color(point.content[0].returnColorType())}',
                                            font = ('New Times Roman',25))


    def quitGame(self):
        self.window.quit()
        self.window.destroy()
        quit()
        
    def mainLoop(self):
        self.window.mainloop()

if __name__ == "__main__":
    GameBoard().mainLoop()

