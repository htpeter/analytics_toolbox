# Analytics Toolbox

## The Main Use Cases

### Importing 

```
import analytics_toolbox as atb
```

## Development

I'm not sure if I want additional help at the moment but if you really want to work with this codebase you can Fork or make a PR. I hope you find value in it. I apologize for my oftentimes odd implementations.

### Want To Develop? Here Are Our Goals

Oftentimes, the efficent data loading, saving, or transformation solution isn't available to you because you have limited time and limited skills. Instead you select something good enough. This projects main goal is to **create a toolkit that helps the user make above average decisions because they are easy.** 

Some examples of this that the API already handles are

1. Keeping multiple database connections efficent and organized.
2. Saving and loading data to S3 efficently. 
3. Loading large amounts of data to servers with limited resoources in a flexible and efficent way. 

#### Use `conda` to create the `atb-dev` environment

This repository uses `conda` as its environment manager.
`conda env create -f environment.yml`

##### If you add a dependency, update  `environment.yml` 

`conda env update --prefix ./env --file environment.yml  --prune`

