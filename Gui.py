# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
import Model
import View
import Control

class Game_board:

    def __init__(self):

        #Game on board
        self.Game = Model.ChessGame();
        
        self.root_window = tk.Tk()

        self.canvas = tk.Canvas(
            master = self.root_window, width = 550, height = 600, background = 'white')
            
        load = Image.open('board.gif')
        render = ImageTk.PhotoImage(load)
        
        self.canvas.create_image(render)
        

        self.canvas.grid(
            row = 0,column = 0,padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.canvas.bind('<Configure>',self._canvas_resizing)
        self.canvas.bind('<Button-1>',self._canvas_clicked)

        self.root_window.rowconfigure(0, weight = 1)
        self.root_window.columnconfigure(0, weight = 1)

    def _draw_base_chunks(self,pixel_w,pixel_h):
        
        for rows in range(0,5):
            for index in range(0,8):
                point_left_top = self.point_list[rows][index]
                point_right_bot = self.point_list[rows+1][index+1]
                
                self.canvas.create_rectangle(pixel_w*point_left_top.fx, pixel_h*point_left_top.fy,
                pixel_w*point_right_bot.fx, pixel_h*point_right_bot.fy,
                fill = 'yellow', outline = 'black')

        river_top_left = self.point_list[4][0]
        river_right_bot = self.point_list[5][8]
        
        self.canvas.create_rectangle(pixel_w*river_top_left.fx, pixel_h*river_top_left.fy,
                pixel_w*river_right_bot.fx, pixel_h*river_right_bot.fy,
                fill = 'red', outline = 'black')
        
        
        for rows in range(5,9):
            for index in range(0,8):
                point_left_top = self.point_list[rows][index]
                point_right_bot = self.point_list[rows+1][index+1]
                
                self.canvas.create_rectangle(pixel_w*point_left_top.fx, pixel_h*point_left_top.fy,
                pixel_w*point_right_bot.fx, pixel_h*point_right_bot.fy,
                fill = 'yellow', outline = 'black')

                
    def _draw_slop_sides(self,pixel_w,pixel_h):
        
        self.canvas.create_line(pixel_w*self.point_list[0][3].fx,pixel_h*self.point_list[0][3].fy,
                                pixel_w*self.point_list[2][5].fx,pixel_h*self.point_list[2][5].fy)
        
        self.canvas.create_line(pixel_w*self.point_list[0][5].fx,pixel_h*self.point_list[0][5].fy,
                                pixel_w*self.point_list[2][3].fx,pixel_h*self.point_list[2][3].fy)
        
        self.canvas.create_line(pixel_w*self.point_list[7][3].fx,pixel_h*self.point_list[7][3].fy,
                                pixel_w*self.point_list[9][5].fx,pixel_h*self.point_list[9][5].fy)

        self.canvas.create_line(pixel_w*self.point_list[7][5].fx,pixel_h*self.point_list[7][5].fy,
                                pixel_w*self.point_list[9][3].fx,pixel_h*self.point_list[9][3].fy)

    def _draw_all_chess(self,pixel_w,pixel_h):
        '''
            draw all chesses
        '''
        radius = 1/25
        for rows in self.point_list:
            for point in rows:
                if point.content[0] != 0 :
                    x = point.fx
                    y = point.fy
                    self.canvas.create_oval(pixel_w*(x-radius), pixel_h*(y-radius),
                pixel_w*(x+radius), pixel_h*(y+radius),
                fill = 'white', outline = 'black')

    def _draw_text_of_chess(self,pixel_w,pixel_h):
        for rows in self.point_list:
            for point in rows:
                if point.content[0] != 0:
                    x = point.fx
                    y = point.fy
                    self.canvas.create_oval(pixel_w*(x-radius), pixel_h*(y-radius),
                pixel_w*(x+radius), pixel_h*(y+radius),
                fill = 'white', outline = 'black')

    def _draw_all_available_move(self,pixel_w,pixel_h):
        pass

    def _canvas_resizing(self,event):
        pixel_w = self.canvas.winfo_width()
        pixel_h = self.canvas.winfo_height()
        
        self.canvas.delete(tkinter.ALL)
        
        self._draw_base_chunks(pixel_w,pixel_h)
        self._draw_slop_sides(pixel_w,pixel_h)
        self._draw_all_chess(pixel_w,pixel_h)
        self._draw_text_of_chess(pixel_w,pixel_h)
        self._draw_all_available_move(pixel_w,pixel_h)
        pass

    def _canvas_clicked(self,event):
        pass

    def cc_game_gui(self):
        '''
            let the board fly
        '''
        self.root_window.mainloop()


if __name__ == "__main__":
    Game_board().cc_game_gui()
    
