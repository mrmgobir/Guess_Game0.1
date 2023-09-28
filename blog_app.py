import os


def create_blog_post():
    title = input("Enter the title of your blog post: ")
    content = input("Enter the content of your blog post:")
    with open(f"{title}.txt", "w") as file:
        file.write(content)
    print("blog post created and saved!")


def view_blog_post():
    title = input("Enter the title of the blog post you want to view:")
    try:
        with open(f"{title}.txt", "r") as file:
            content = file.read()
        print(f"***{title}***\n{content}")
    except FileNotFoundError:
        print("Blog post does not exist")


def delete_blog_post():
    title = input("Enter the title of the post you want to delete")
    print("Are you sure you want to delete this post?")
    confirmation = input("yes or no  ")
    if confirmation == "yes":
        try:
            os.remove(f"{title}.txt")
            print("Blog post deleted")
        except FileNotFoundError:
            print("Blog post was not found")
    elif confirmation == "no":
        print(f"{title}.txt not deleted")
    else:
        print("Invalid Option")


while True:
    print("Options")
    print("1 - Create Blog Post")
    print("2 - View Blog Post")
    print("3 - Delete Blog Post")
    print("4 - Exit")
    options = input("Enter your choice:")

    if options == "1":
        create_blog_post()
    elif options == "2":
        view_blog_post()
    elif options == "3":
        delete_blog_post()
    elif options == "4":
        break

    else:
        print("Invalid Input!")

