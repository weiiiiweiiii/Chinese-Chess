#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:55:35 2017

@author: Yuliangze
"""

##Chess names：
##    Red Black
##0 = blank
##1 = 帥  將  king
##2 = 仕  士  guard
##3 = 相	象   elephant
##4 = 傌	馬   horse
##5 = 俥	車   tank
##6 = 炮	砲   cannon
##7 = 兵	卒   soldier

# If one day we could combine those chess into a new good chess
# That would help us lot to create a whole new game

"""
data from game board

horizontal data:
48 42 670 670
120 42 670 670

D_HORIZONTAL = 0.10746268656716418 

veritical data:
120 42 670 670
120 108 670 670
    
D_VERTICAL = 0.09850746268656717

padding :
x:48 y:43 window_x:670 window_y:670

padding x = 0.07164179104477612
padding y = 0.06417910447761194
"""

CC_BOARD_SEQUENCE = '543212345000000000060000060707070707000000000000000000707070707060000060000000000543212345'

PADDING_X = 0.07164179104477612        #padding between frame
PADDING_Y = 0.06417910447761194

D_VERTICAL = 0.09850746268656717    #each rectangle vertical side
D_HORIZONTAL = 0.10746268656716418       #each rectangle horizontal side

CHESS_RADIUS = 1/23


'''
Board Game
'''
class ChessGame:
    
    def __init__(self,gameBoard):
        self._gameState = gameBoard
            
    def __iter__(self):
        class Generator:
            def __init__(self,grids):
                self.index = -1
                self.gridList = grids
            
            def __next__(self):
                self.index+=1
                if self.index >= len(self.gridList):
                    raise StopIteration
                return self.gridList[self.index] 
        return Generator(self._gameState)
    
    def returnBoard(self):
        return self._gameState
  
'''
Chess Type
'''              
    
class Chess:
    def __init__(self,typeNum,color):
        self._color = color
        self._identity = typeNum

    def returnWholeType(self):
        return self.__repr__()
    
    def returnNumType(self):
        return self._identity
        
    def returnColorType(self):
        return self._color

class Guard(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)

    def __str__(self):
        if self._color == 'b':
            return '士'
        return '仕'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'
    

class Soldier(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)

    def __str__(self):
        if self._color == 'b':
            return '卒'
        return '兵'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'
    
        
class Cannon(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)

    def __str__(self):
        if self._color == 'b':
            return '砲'
        return '炮'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'
    
    
class Tank(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)
    
    def __str__(self):
        if self._color == 'b':
            return '車'
        return '俥'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'
    
class Elephant(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)

    def __str__(self):
        if self._color == 'b':
            return '象'
        return '相'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'
    
class Horse(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)

    def __str__(self):
        if self._color == 'b':
            return '馬'
        return '傌'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'
    
class King(Chess):
    
    def __init__(self,type_num,color):
        Chess.__init__(self,type_num,color)
        
    def __str__(self):
        if self._color == 'b':
            return '將'
        return '帥'
    
    def __repr__(self):
        return f'({self._identity},{self._color})'


'''
BasePoints
'''



class BasePoint:
    def __init__(self, fx: float, fy: float,chess):
        '''
            initila the point
        '''
        self.fx = fx
        self.fy = fy
        self.content = [chess]

    def fraction(self) -> (float, float):
        '''
            fraction of point
        '''
        return (self.fx, self.fy)


    def pixel(self, pixel_width: int, pixel_height: int) -> (float, float):
        '''
            pixel of point
        '''
        return (self.fx * pixel_width, self.fy * pixel_height)

    def digital_identity(self):
        if self.content[0] == 0:
            return 0
        return repr(self.content[0])

    def string_identity(self):
        if self.content[0] == 0:
            return 0
        return str(self.content[0])


def from_frac(frac_x: float, frac_y: float) -> BasePoint:
    '''
        from fraction of point
    '''
    return BasePoint(frac_x, frac_y)


def from_pixel(pixel_x: int, pixel_y: int, pixel_width: int, pixel_height: int) -> BasePoint:
    '''
        from pixel of point
    '''
    return BasePoint(pixel_x / pixel_width, pixel_y / pixel_height)
        

