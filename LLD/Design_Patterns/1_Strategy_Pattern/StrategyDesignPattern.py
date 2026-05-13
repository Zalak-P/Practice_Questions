# ======================================================
# STRATEGY FAMILY 1 --> WALK
# ======================================================

class WalkableRobot:
    def walk(self):
        pass

# ---------------- WALK STRATEGIES ----------------

class NormalWalk(WalkableRobot):
    def walk(self):
        print("Walking normally...")

class NoWalk(WalkableRobot):
    def walk(self):
        print("Cannot walk.")

# ======================================================
# STRATEGY FAMILY 2 --> TALK
# ======================================================

class TalkableRobot:
    def talk(self):
        pass
# ---------------- TALK STRATEGIES ----------------

class NormalTalk(TalkableRobot):
    def talk(self):
        print("Talking normally...")

class NoTalk(TalkableRobot):
    def talk(self):
        print("Cannot talk.")

# ======================================================
# STRATEGY FAMILY 3 --> FLY
# ======================================================

class FlyableRobot:
    def fly(self):
        pass

# ---------------- FLY STRATEGIES ----------------

class NormalFly(FlyableRobot):
    def fly(self):
        print("Flying normally...")

class NoFly(FlyableRobot):
    def fly(self):
        print("Cannot fly.")

# ======================================================
# ROBOT BASE CLASS
# ======================================================

class Robot:

    # Inject strategies during object creation
    def __init__(self, walk_behavior, talk_behavior, fly_behavior):
        self.walk_behavior = walk_behavior
        self.talk_behavior = talk_behavior
        self.fly_behavior = fly_behavior

    # Delegate behavior to strategy object
    def walk(self):
        self.walk_behavior.walk()

    def talk(self):
        self.talk_behavior.talk()

    def fly(self):
        self.fly_behavior.fly()

    def projection(self):
        pass

# ======================================================
# CONCRETE ROBOTS
# ======================================================

class CompanionRobot(Robot):
    def projection(self):
        print("Displaying friendly companion features...")

class WorkerRobot(Robot):
    def projection(self):
        print("Displaying worker efficiency stats...")

# ======================================================
# MAIN
# ======================================================

# Robot 1 uses:
# Normal walking
# Normal talking
# No flying
robot1 = CompanionRobot(
    NormalWalk(),
    NormalTalk(),
    NoFly()
)
robot1.walk()
robot1.talk()
robot1.fly()
robot1.projection()

print("--------------------")

# Robot 2 uses:
# No walking
# No talking
# Normal flying

robot2 = WorkerRobot(
    NoWalk(),
    NoTalk(),
    NormalFly()
)

robot2.walk()
robot2.talk()
robot2.fly()
robot2.projection()