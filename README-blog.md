# Publishing a Blog Post

## Tl;dr

Duplicate the [example post file](main/blog/posts/tutorials/yyyy-mm-dd--EXAMPLE_POST_1.md) in-place and update the header parameters and filename.

If you will use images, copy the [example post folder](main/blog/posts/tutorials/yyyy-mm-dd--EXAMPLE_POST_2) instead and store you images inside.

> [!NOTE]
> **No need to clone this repo**
> You can add or edit posts directly on GitHub and they will be published immediately unless `draft: true` is set.

<br><br>


## Guidelines

- Follow basic instructions inside the template.
- Whenever possible, include an image with your blog post, this will be in the preview when you post gets shared.

    ```
    ![alt text](my-image.jpg)
    ```
- Start your tutorial titles with "How to", think SEO when you choose a title.
- Store images in he same folder as your post.
- Add the date to the markdown filename or the parent folder, so things stay organized.
- Check [style-reference.md](../docs/style-reference.md) to see how to use buttons, icons, admonitions etc. See the [HTML output here](https://openad.accelerate.science/style-reference).
- Tip: two spaces at the end of a line create a line break.
- If your post is not a tutorial, publish it under [/general](main/blog/posts/general) instead.

<br><br>

## Notes

-   Any updates pushed to the `main` branch will immediately be deployed.
-   Deployment takes about 2-3 minutes, progress can be followed under the [Actions](../../actions) tab.












