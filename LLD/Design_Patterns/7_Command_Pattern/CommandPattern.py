from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class Fan:
    def on(self):
        print("Fan is ON")

    def off(self):
        print("Fan is OFF")

class LightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class FanCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()

class RemoteController:
    NUM_BUTTONS = 4

    def __init__(self):
        self.buttons = [None] * self.NUM_BUTTONS
        self.button_pressed = [False] * self.NUM_BUTTONS

    def set_command(self, index, command):
        if 0 <= index < self.NUM_BUTTONS:
            self.buttons[index] = command
            self.button_pressed[index] = False

    def press_button(self, index):
        if not (0 <= index < self.NUM_BUTTONS) or self.buttons[index] is None:
            print(f"No command assigned at button {index}")
            return

        if not self.button_pressed[index]:
            self.buttons[index].execute()
        else:
            self.buttons[index].undo()

        self.button_pressed[index] = not self.button_pressed[index]

if __name__ == "__main__":
    living_room_light = Light()
    ceiling_fan = Fan()

    remote = RemoteController()

    remote.set_command(0, LightCommand(living_room_light))
    remote.set_command(1, FanCommand(ceiling_fan))

    print("--- Toggling Light Button 0 ---")
    remote.press_button(0)
    remote.press_button(0)

    print("--- Toggling Fan Button 1 ---")
    remote.press_button(1)
    remote.press_button(1)

    print("--- Pressing Unassigned Button 2 ---")
    remote.press_button(2)

# Expected Output
# ---------------

# --- Toggling Light Button 0 ---
# Light is ON
# Light is OFF

# --- Toggling Fan Button 1 ---
# Fan is ON
# Fan is OFF

# --- Pressing Unassigned Button 2 ---
# No command assigned at button 2