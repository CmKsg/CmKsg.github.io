---
title: "Game Optimization with Recurrent Neural Network"
collection: projects
permalink: /projects/gameoptimizer
excerpt: 'An RNN that will predict optimal outcomes.'
date: 2025-08-01
venue: ''
---

I play this retro simple RPG game, in which your characters collect coins on a recurring loop, similar to an idle game like Cookie Clicker or AdVenture Capitalist. The intricacy of the game comes from it's skilling system, in which you have limited amount of skill points (limited by the amount of time it takes to gain XP), and must spend those skill points wisely to ensure maximum coin collection. 

I've tried to optimize this in 3 separate ways with different success:

1) Traditional Optimization (OR using mixed-IP): using a traditional optimizer like Gurobi, which uses an approximation algorithm should have been the most straight forward answer. However, most optimizers (scipy, Gurobi and many others I've tried), fail at handling non-linear functions and enacting strict constraints. The game has strict tier unlock constraints and quadratic reward functions, so no optimizer could solve the problems feasibly.
2) Greedy/Beam Search: using a greedy method gave results. The reward function, besides the tier constrain and quadratic aspect of it, was fairly easy and efficient to set up, with some issues arising from derivative approximation of the reward. This was my main working solution, as it gave a clear answer with a clear result.
3) Dynamic Programming: this would be the best solution if it was possible. The issue with the dynamic programming is that the skill points in the game reach a maximum of 5 so there would be roughly 5.3*10^53 possible outcomes to calculate for just 30 levels (the maximum level is around 265). This would make calculation impossible, especially for the web-app I was designing to handle it.

So, for my web-app, I went ahead with the greedy algorithm. It was still received well, but I always had in the back of my mind a yearning for a better solution. This is when one day I thought of using a neural network.

The neural network would do what dynamic programming did, except much more efficiently as it would essentially lock out non-reward providing skills. It would also work greatly for the variation in characters (high defensiveness vs. high collection speed), as it could learn relations between the different skillpoints in the game easily. Finally, I would also be able to put in place the tier unlock constraint that I was struggling with, by giving large negative rewards for trespassing it, and teaching the network to not violate the constraint.
