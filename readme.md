# Keywordcloud generator using AWS Lambda
Use this script to create a word cloud image generator using AWS Lambda and S3.
Lambda trigger: upload background image (png) to s3 bucket


## Set up instructions:

- [ ] Create AWS S3 bucket, create folder for image uploads, create folder for output png files (the word cloud png files generated)
- [ ] Create AWS Lambda Function
- [ ] Github Actions: test and deploy to AWS Lambda
- [ ] Upload a text file and a backgound image to the S3 bucket and check for output file

If everything is set up correctly you should be able to see an output file with a word cloud every time you upload a new png file. There must be a matching text file with the same name as the png file or the script will look for a default txt file for keywords. Example: batman-bg.png batman-bg.txt. Default text file: default.txt

## Planned Integration with website
SEO web tools: [amzto.com](https://amzto.com) -- add python app as micro service (new tool) and integrate in site's menu.

## Credits & Resources:
Special thanks to NeuralNine for the original code base and idea for this project: 
[Create Fancy Word Clouds in Python - NeuralNine](https://www.youtube.com/watch?v=vRbSnlRyJNQ)
[Word Cloud in python | Word cloud tutorial](https://www.youtube.com/watch?v=4N_exdTyGHk)

[AWS Lambda with S3 Trigger Example](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)
[Tutorial: Using an Amazon S3 trigger to create thumbnail images with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html)

[Stylecloud tutorial](https://www.youtube.com/watch?v=txPNMDDWsB8)
[Fontawesome version 5.x](https://github.com/minimaxir/stylecloud)
[Fontawesome Icons](https://fontawesome.com/icons)