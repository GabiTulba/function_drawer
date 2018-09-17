import pyglet
import sys
import sympy

alpha={pyglet.window.key._0:'0', pyglet.window.key._1:'1', pyglet.window.key._2:'2', pyglet.window.key._3:'3', pyglet.window.key._4:'4', pyglet.window.key._5:'5', pyglet.window.key._6:'6', pyglet.window.key._7:'7', pyglet.window.key._8:'8', pyglet.window.key._9:'9', pyglet.window.key.A:'a', pyglet.window.key.B:'b', pyglet.window.key.C:'c', pyglet.window.key.D:'d', pyglet.window.key.E:'e', pyglet.window.key.F:'f', pyglet.window.key.G:'g', pyglet.window.key.H:'h', pyglet.window.key.I:'i', pyglet.window.key.J:'j', pyglet.window.key.K:'k', pyglet.window.key.L:'l', pyglet.window.key.M:'m', pyglet.window.key.N:'n', pyglet.window.key.O:'o', pyglet.window.key.P:'p', pyglet.window.key.Q:'q', pyglet.window.key.R:'r', pyglet.window.key.S:'s', pyglet.window.key.T:'t', pyglet.window.key.U:'u', pyglet.window.key.V:'v', pyglet.window.key.W:'w', pyglet.window.key.X:'x', pyglet.window.key.Y:'y', pyglet.window.key.Z:'z', pyglet.window.key.PARENLEFT:'(', pyglet.window.key.PARENRIGHT:')', pyglet.window.key.PLUS:'+', pyglet.window.key.MINUS:'-', pyglet.window.key.ASTERISK:'*', pyglet.window.key.SLASH:'/', pyglet.window.key.PERIOD:'.', pyglet.window.key.PERCENT:'%', pyglet.window.key.SPACE:' ', pyglet.window.key.COMMA:','}
expr=''
dummy_func=sympy.sympify('1')
Insert=False
Width,Height=(960,720)
Center=(Width/2,Height/2)
screen = pyglet.window.Window(width = Width, height = Height)

def Draw_function():
	global expr
	try:
		func=sympy.sympify(expr)
		for i in range(-Center[0],Center[0]):
			if(type(func.subs('x',float(i)).evalf())!=type(dummy_func.evalf()) or type(func.subs('x',float(i+1)).evalf())!=type(dummy_func.evalf())):
				continue
			else:
				pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', (float(i)+Center[0], func.subs('x',float(i)).evalf()+Center[1], float(i)+1+Center[0], func.subs('x',float(i+1)).evalf()+Center[1] )))
	except: 
		return
@screen.event
def on_key_press(symbol, modifiers):
    global Insert,expr
    if symbol == pyglet.window.key.ESCAPE:
	screen.close()
    elif symbol == pyglet.window.key.ASCIITILDE:
	if Insert:
		Insert=False
	else: Insert=True
    elif Insert and symbol in alpha:
	expr += alpha[symbol]
    elif Insert and symbol == pyglet.window.key.BACKSPACE:
	expr = expr[:-1]
@screen.event
def on_draw():
	screen.clear()
	pyglet.graphics.draw_indexed(4, pyglet.gl.GL_LINES, [0,2,1,3], ('v2i', (0, Height/2, Width/2, 0, Width, Height/2, Width/2, Height) ) )
	write=[	
		pyglet.text.Label('To exit press esc', font_name='Arial',anchor_y='top', font_size=14, x=5, y=Height-5),
		pyglet.text.Label('Insert mode: {}.'.format(Insert), font_name='Arial',anchor_y='top', font_size=14, x=5, y=Height-25),
		pyglet.text.Label('In order to toggle Insert mode press ~', font_name='Arial',anchor_y='top', font_size=14, x=5, y=Height-45),
		pyglet.text.Label('f(x) = {}'.format(expr), font_name='Arial',anchor_y='top', font_size=14, x=5, y=Height-65)
		]
	for x in write:
		x.draw()
	Draw_function()
pyglet.app.run()
