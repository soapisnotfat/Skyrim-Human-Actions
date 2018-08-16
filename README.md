# ES5-Skyrim-Human-Actions

This is a human action dataset collected from Elder Scrolls V: Skyrim.

## Categories

This dataset contains **10** categories: 5 of them are the categories that are included in UCF101, and the other 5 categories are not. Each catefory has 10 videos, and each video lasts 5 seconds. The resolution of all videos is 320x180. The native FPS is 30.

### 5 included in UCF101

- archery
  - https://www.youtube.com/watch?v=V9e0T6i8Vkw
- horse riding
  - https://www.youtube.com/watch?v=BQX3yswJDtE
  - https://www.youtube.com/watch?v=QQDbqu99f18
  - https://www.youtube.com/watch?v=OiXxJGFEn3A
- run (floor gymnastics)
  - https://www.youtube.com/watch?v=TD9mBn3ZmjI
  - https://www.youtube.com/watch?v=0oaFf2sAS68
- breaststroke
  - https://www.youtube.com/watch?v=WylQDP7GWqg
  - https://www.youtube.com/watch?v=I69k4vJTdtg
- skydiving
  - https://www.youtube.com/watch?v=5KprI6hCN-8
  - https://www.youtube.com/watch?v=n59YApQW7nM

### 5 completely new

- crossbow
  - https://www.youtube.com/watch?v=iA65eNuV7UQ
- dance
  - https://www.youtube.com/watch?v=zNr-Vfy3eXU
- dodge
  - https://www.youtube.com/watch?v=sak77CCuxR4
- fly
  - https://www.youtube.com/watch?v=5lc_Aki3vvc
- waving weapon
  - https://www.youtube.com/watch?v=M3pKL6Ch1aU

## Installation

Github:

```sh
git clone https://github.com/IvoryCandy/Skyrim-Human-Actions.git
```

## frame extraction

The frame extraction is provided along with the repo.

Requirement:

- python3
- ffmpeg

### Usage

```sh
python3 extract_frame.py
```

## Meta

Zijin Luo – zijinluo@gatech.edu

Distributed under the Apache2 license. See ``LICENSE`` for more information.

## Contributing

- [Fork it](https://github.com/IvoryCandy/Skyrim-Human-Actions/fork)
- Create a new Pull Request
