# Roshambo-Lite

## Demo

[![RPS_Demo_Video](http://img.youtube.com/vi/D4GdTonzPJk/0.jpg)](http://www.youtube.com/watch?v=D4GdTonzPJk "Demo Video")

## Inspiration
Big Bang Theory and [RPS Games](http://www.umop.com/rps.htm)

## What it does
The application uses the best of three rounds to determine the winner of the game .The player gets to advance to the next round, only when either the droid or the player wins. Make the hand gesture for either rock, paper or scissor before the timer runs out. The image captured when the timer runs out will be used for identification. The droid picks a gesture based on a random gesture generator. The winner of the round is decided based on the classic rules of rock , paper and scissors. 

## How I built it
The first step was collecting hand gestures for building a dataset for Roshambo classification.The dataset looked decent after data augmentation.Then I trained a neural network to recognize the gestures. The last step was to design an android app that can deploy the trained model.

## Challenges I ran into
The model trained does not generalize . i.e. the model identifies the gestures made by people, from whom I collected the images to build the dataset, with more accuracy than the gestures from a stranger. To avoid this, either  a more diverse dataset for training must be built or another algorithm (tracking fingertips and their relative positions) to identify the hand gestures used must be developed.

## What's next for RoShamBo Lite:
1. Build the dataset so that so that the extended version of this classic game could be played.
2. Roshambo League , where players can compete against each other online.
3. Implement a screening mechanism, so that only valid hand gestures are recognized .
4. Make the computer intelligent , i.e. incorporate learning algorithms when playing against the computer .
