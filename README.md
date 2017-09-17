# MySolusRepo
3rd Party Repo for Solus by me 

## Build and Install via eopkg

### Step 1: Build Pkg
```sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/swerner1511/MySolusRepo/master/programming/idea-ce/pspec.xml```

### Step 2: Install Pkg
```sudo eopkg it idea*.eopkg;sudo rm idea*.eopkgsudo eopkg bi --ignore-safety```
