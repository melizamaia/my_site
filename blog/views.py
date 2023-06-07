from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.png",
        "author": "Gooogle Images",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            In today’s world of chaos and constant stimulation, it’s hard to quiet the mind and think.
            
            Getting into Nature offers a way to find some silence and clarity; and it’s an important tool to counter our standards of survival in society.
            The more and more pressure we put on ourselves, the more our health degrades. Our minds and bodies need silence in order to regenerate.

        
            We choose hikes based on how capable we are feeling or the size of the challenge we want. In either case, we end up mentally feeling the same: accomplished and clear minded.
            Everyday stressors seem so small and we are motivated to let the damaging things in our lives go.
            
            
            It seems the cocktail of Hiking and Nature is a remedy for unclogging the mind of the unnecessary and allowing us to focus on the bigger picture.
            The speed of life, these days, seems to crowd our brains with too much information. With the clarity we gain from hiking, inspiration can pour in.
            
            I go to nature to be soothed and healed, and to have my senses put in order. ~John Burroughs
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Google Images",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
            Programming is a rewarding and empowering skill that opens up a world of possibilities. It offers numerous advantages and brings with it a sense of fulfillment and joy. Let's explore some of the reasons why programming is so good:
            
            
            Problem-Solving: Programming helps you develop problem-solving skills by breaking down complex issues into manageable parts and finding creative solutions.


            Creativity: Programming allows you to unleash your creativity by designing and building unique applications or websites from scratch.


            Continuous Learning: Programming is a field that offers endless opportunities to learn and grow. There's always something new to explore, keeping your mind engaged and expanding your knowledge.


            Building Practical Solutions: With programming, you can create useful tools and applications that make people's lives easier or solve specific problems in various industries.


            Collaboration: Programming often involves working with others, fostering teamwork and the opportunity to exchange ideas and learn from peers.


            Flexibility and Remote Work: Programming provides the flexibility to work remotely and choose your own hours, offering a good work-life balance.


            Automation: Programming allows you to automate repetitive tasks, saving time and increasing efficiency in various aspects of work and daily life.


            Job Opportunities: The demand for skilled programmers is high, providing ample job opportunities and career growth potential.


            Sense of Accomplishment: Seeing your code come to life and function as intended can bring a great sense of satisfaction and accomplishment.


            Making a Positive Impact: Through programming, you can develop applications that have a real impact on people's lives, whether it's improving accessibility, education, or communication.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.png",
        "author": "Google Images",
        "date": date(2020, 8, 5),
        "title": "Nature gives you hopes",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
            You don’t need to live by the beach or move to the country to enjoy the benefits of nature. Here are some easy ways to get a nature boost, no matter where you live.

            Get up early to watch the sunrise and start the day.

            Eat as many meals as you can outside.

            Exercise outdoors instead of inside.

            Go for a daily walk.

            Have a coffee break by taking a stroll around the garden or block.

            Read your book outside – sitting under a tree or lying down on the grass.

        """
    }
]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })