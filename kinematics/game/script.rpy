# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image rectangle = Crop ((0,0, 300, 50), Solid("fff"))
image rec2 = Crop ((0,0, 300, 50), Solid("f00"))
image rec3 = At(rotation(0, 0, 0, 0, 3), Crop ((0,0, 300, 50), Solid("0f0")))



# The game starts here.

transform rotation (posx, posy, rotx, roty, a):
  around (rotx, roty)
  alignaround (rotx, roty)
  xalign rotx
  yalign roty
  xpos posx
  ypos posy
  transform_anchor True
  function renpy.curry(transformrotation)(a=a)

layeredimage rec2l:
  always:
     Crop ((0,0, 300, 50), Solid("f00"))
     at rotation(300, 0, 0, 0, 2)




init python:
  angle = 0
  angle2 = 0
  angle3 = 0
  def transformrotation(trans, st, at, a):
    print (a)
    if a == 1:
      trans.rotate = angle
    elif a == 2:
      trans.rotate = angle2
    elif a == 3:
      trans.rotate = angle3
    return 0
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    
    
    show rectangle at rotation (100, 800, 0, 0, 1)
    show rec2 at rotation (100+300, 800, 0, 0, 2)
    show rec3 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
      "set angle (e.g. -30)":
          python:
              angle = int(renpy.input("angle?", length=32))
          hide rectangle
          hide rec2
          show rectangle at rotation (100, 800, 0, 0, 1)
          show rec2 at rotation (100+300, 800, 0, 0, 1)
          e "Not right"
          hide rec2
          show rec2 at rotation (100, 800, 0, 0, 1), rotation (300, 800, 0, 0, 2)
          e "Not right either"
          hide rec2
          show rec2 at rotation (300, 800, 0, 0, 2), rotation (100, 800, 0, 0, 1)
          e "This does not work either"
          hide rec2
          show rec2l at rotation (100, 800, 0, 0, 1)
          e "right, the transforms are composed"
      "continue":
          pass

    menu:
      "set angle 2 (e.g. -45)":
          python:
              angle2 = int(renpy.input("angle?", length=32))
          hide rec2l
          show rec2l at rotation (100, 800, 0, 0, 1)
          e "the transforms are still being composed"
      "continue":
          pass

    menu:
      "set angle 3 (e.g. -10)":
          python:
              angle3 = int(renpy.input("angle?", length=32))
          e "How can this transform be composed with the other two?"
          e "And why is rec3 not even showing?"
      "continue":
          pass

    

    return
