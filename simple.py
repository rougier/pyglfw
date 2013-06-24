# -----------------------------------------------------------------------------
#  GLFW - An OpenGL framework
#  API version: 3.0.1
#  WWW:         http://www.glfw.org/
#  ----------------------------------------------------------------------------
#  Copyright (c) 2002-2006 Marcus Geelnard
#  Copyright (c) 2006-2010 Camilla Berglund
#
#  Python bindings - Copyright (c) 2013 Nicolas P. Rougier
#  
#  This software is provided 'as-is', without any express or implied
#  warranty. In no event will the authors be held liable for any damages
#  arising from the use of this software.
#  
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#  
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would
#     be appreciated but is not required.
#  
#  2. Altered source versions must be plainly marked as such, and must not
#     be misrepresented as being the original software.
#  
#  3. This notice may not be removed or altered from any source
#     distribution.
#  
# -----------------------------------------------------------------------------
#
# This short example shows how the GLFW API looks and how easy it is to create
# and a window and OpenGL context with it. There are many more functions than
# those used here, but these are all you need to get started.
#
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    import glfw
    import OpenGL.GL as gl

    def on_key(window, key, scancode, action, mods):
        if key == glfw.KEY_ESCAPE:
            glfw.SetWindowShouldClose(window,1)

    # Initialize the library
    if not glfw.Init():
        sys.exit()

    # Create a windowed mode window and its OpenGL context
    window = glfw.CreateWindow(640, 480, "Hello World", None, None)
    if not window:
        glfw.Terminate()
        sys.exit()

    # Make the window's context current
    glfw.MakeContextCurrent(window)

    # Install a key handler
    glfw.SetKeyCallback(window, on_key)

    # Loop until the user closes the window
    while not glfw.WindowShouldClose(window):
        # Render here
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Swap front and back buffers
        glfw.SwapBuffers(window)

        # Poll for and process events
        glfw.PollEvents()

    glfw.Terminate()
