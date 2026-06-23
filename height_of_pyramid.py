print(43 * "#")
print("## height of the pyramid based on blocks.##")
print(43 *"#")
blocks = int(input("Enter the number of blocks: "))
height=0
blocks_per_step=1
while blocks_per_step <= blocks:              # loop untill the blocks per step remaing less tahn or equal to total blocks.
    height+=1                                 # first step of pyramid
    blocks-=blocks_per_step                   # remaining blocks after step N
    blocks_per_step+=1                        # blocks for next steps of pyramid
print("The height of the pyramid:", height)
