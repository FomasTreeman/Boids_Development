from AppSetup import *
from AgentLib import *
import random


class Model:
    def __init__(self):
        self.max_length = 100
        self.cohesion = Vector2D(0, 0)
        self.separation = Vector2D(0, 0)
        self.alignment = Vector2D(0, 0)
        # self.agents = [AgentLib(random.randint(10, 990), random.randint(10, 590)) for i in range(50)]
        self.agents = [AgentLib(random.randint(50, 900), random.randint(50, 500)) for i in range(50)]

    def setup(self, window: tk.Canvas):
        for agent in self.agents:
            agent.velocity = Vector2D(random.randint(-50, 50), random.randint(-100, 100))

            agent.setup(window)

        # distance = agent.position - self.position
        #     if distance.mag() <= 100:
        #         self.sum_velocity += agent.velocity
        #         agent.apply_force(0.1)

    def draw(self, window: tk.Canvas):
        sum_position = Vector2D(0, 0)
        mean_position = Vector2D(0, 0)
        sum_velocity = Vector2D(0, 0)

        # draw whos near me
        for agent in self.agents:
            count = 0
            for other_agent in self.agents:
                count += 1
                # distance = agent.position - other_agent.position
                # sum_velocity += agent.velocity
                # if distance.mag() <= 100:
                #     sum_position += other_agent.position
                #     count += 1
                # if count == 0:
                #     mean_position = agent.position
                # else:
                #     mean_position = sum_position / count
                #     self.alignment = sum_velocity / count
                # # separation
                # self.cohesion = mean_position - agent.position
                # self.separation = self.cohesion
                # self.separation *= - 1
                # mag = self.separation.mag()
                # self.separation = self.separation.norm() * (self.max_length - mag)
                # sum_velocity = self.alignment + self.separation + self.cohesion

# separation

                distance = agent.position - other_agent.position
                if distance.mag() <= 20:
                    distance *= -1
                    other_agent.apply_force(distance * 0.1)
                    sum_velocity += other_agent.velocity
# cohesion

                if distance.mag() <= 150:
                    sum_position += other_agent.position


# alignment
            if sum_position or sum_velocity == 0:
                pass
            else:
                sum_position /= count
                velocity = sum_position - agent.position

                sum_velocity /= count
                velocity += sum_velocity

                agent.apply_force(velocity * 0.01)

            # agent.apply_force(sum_velocity * 0.01)
            agent.update()
            agent.edges(window)
            agent.display(window)

        # window.coords(self.separation, self.position.x, self.position.y, self.position.x + velocity.x,
        #               self.position.y + velocity.y)
        #
        # velocity = self.sum_velocity / count
        #
        # window.coords(self.alignment, self.position.x, self.me.position.y,
        #               self.position.x + velocity.x, self.me.position.y + velocity.y)
        #
        # mean_pos_dist = mean_position - self.position
        # window.coords(self.cohesion, self.position.x, self.position.y, self.position.x + mean_pos_dist.x,
        #               self.position.y + mean_pos_dist.y)


model = Model()
app = App("Boids attempt 1", model)
app.mainloop()
