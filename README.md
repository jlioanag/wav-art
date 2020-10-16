# wav-art
### Taking wav files and making generative art

![Example pic](./examples/slide_10000_1.0.png)

## How it works
* Uses pydub to get array of data samples from an `.mp3` or `.wav` file.
* Each data point functions as a ruleset for an [Elementary Cellular Automaton](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html).
* The Cellular Automaton is plotted with matplotlib and layered over with each data point.
## Dependencies
* Python 3.7+
  * pydub, matplotlib
## Examples
All of the images on this page are generated from a certain amount of samples from Calvin Harris' song, Slide.
Here are the sample sizes in order (top-to-bottom): `10000`, `1000`, `2`.

![Example pic](./examples/slide_1000_1.0.png)
![Example pic](./examples/slide_2_1.0.png)
