---
title: Custom Page Title
# subtitle: My Milkshake etc.
status: new
hide:
    - navigation
---

# Style Reference

This file contains examples on how to style markdown for the OpenAD website.

---

## Buttons

[Primary Button](#){ .md-button .md-button--primary }
[Secondary Button](#){ .md-button }
[Tertiary Button](#){ .md-button .md-button--tertiary }

[:carbon-icn-bee: Primary Button](#){ .md-button .md-button--primary }
[:carbon-icn-bee: Secondary Button](#){ .md-button }
[:carbon-icn-bee: Tertiary Button](#){ .md-button .md-button--tertiary }

[Primary Button](#){ .md-button .md-button--primary .btn-large }
[Secondary Button](#){ .md-button .btn-large }
[Tertiary Button](#){ .md-button .md-button--tertiary .btn-large }

---

## Links

[Unique link](https://example.com "With a unique tooltip")

[Repeated link] / [Repeated link] / [Repeated link]

[Repeated link]: https://example.com "With a repeated tooltip"

---

## Icons

:carbon-icn-bee:
:carbon-icn-link:
:carbon-icn-machine-learning:
:carbon-icn-megaphone:
:carbon-icn-yes:{ style="color: var(--carbon-success)"" }
:carbon-icn-no:{ style="color: var(--carbon-error)"" }

:carbon-icn-yes:{ .inline } I'm an inline icon

<small>:carbon-icn-yes:{ .inline } I'm an inline icon in small text</small>

<br>

Useful HTML characters:

&uarr; Up arrow  
&darr; Down arrow  
&larr; Left arrow  
&rarr; Right arrow  
&harr; Double headed arrow  

---

## Flags

**Flag**{ .flag }
**Flag**{ .flag .green }
**Flag**{ .flag .yellow }
**Flag**{ .flag .orange }
**Flag**{ .flag .red }
**Flag**{ .flag .blue }

I'm a regular text **flag**{ .flag } inline

<small>I'm a small text **flag**{ .flag } `inline next to code`</small>

---

## Images

Regular image:

![image](_assets/home/screen-cli.png)

Retina display screenshit with correct pixel width set:

![image](_assets/home/screen-cli.png){ width=652 }

Image with custom styling:

![image](_assets/home/screen-cli.png){ width=652 style='border: solid 10px var(--carbon-blue)' }

Browser screenshot from macOS Chrome with shadow:

![image](blog/posts/tutorials/plugins/01-create-plugin/mol-with-fp_ap.png){ width=752 .browser-ss }

Terminal screenshot from macOS in full-width box:

<p class="cli-ss-wrap" markdown>
    ![OpenAD CLI](_assets/home/screen-cli.png){ width="652" style="max-width: 100%" }
</p>

---

## Admonitions

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! abstract

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! info

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! tip

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! success

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! question

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! warning

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! failure

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! danger

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! bug

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! example

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! quote

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

---

<details>
<summary>Expandable section</summary>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum</p>

<p>Note: expanding headers are not picked up by the table of contents, nor are markdown rules applied inside.</p>

</details>

<details>
<summary><h2>Expandabable Section Header</h2></summary>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.</p>

<p>Note: expanding headers are not picked up by the table of contents, nor are markdown rules applied inside.</p>

</details>

<details>
<summary><h3>Expandabable Section Header</h3></summary>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.</p>

<p>Note: expanding headers are not picked up by the table of contents, nor are markdown rules applied inside.</p>

</details>

<details>
<summary><h4>Expandabable Section Header</h4></summary>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.</p>

<p>Note: expanding headers are not picked up by the table of contents, nor are markdown rules applied inside.</p>

</details>

<details>
<summary><h5>Expandabable Section Header</h5></summary>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.</p>

<p>Note: expanding headers are not picked up by the table of contents, nor are markdown rules applied inside.</p>

</details>

---

## Code Blocks

Here is some `hello world` inline code.

Code block python:

```python
print("hello world")
```

Code block JS:

```javascript
console.log('hello world')
```

Code block CLI

```shell
pip install hello-world
```

---

## Tables

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

---

## Text styles

**Lorem ipsum dolor sit amet, consectetur adipiscing elit.** _Nam gravida gravida euismod. Aliquam erat volutpat._ In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. <em>Nulla ac urna elit.</em> Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

<small>**Lorem ipsum dolor sit amet, consectetur adipiscing elit.** _Nam gravida gravida euismod. Aliquam erat volutpat._ In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. <em>Nulla ac urna elit.</em> Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.</small>

<div class="xsmall"><b>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</b> <i>Nam gravida gravida euismod. Aliquam erat volutpat.</i> Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. <em>Nulla ac urna elit.</em> Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.</div>

---

## Lists

<div class="padded-list" markdown>
- This is a padded list, looks better when there's code blocks in the list.

    ```shell
    foo bar
    ```

- This is a padded list, looks better when there's code blocks in the list.

    ```shell
    foo bar
    ```

<div class="tight-list" markdown>

- This is a tight list inside a padded list.
- This is a tight list inside a padded list.
- This is a tight list inside a padded list.

</div>

- This is a padded list, looks better when there's code blocks in the list.

    ```shell
    foo bar
    ```

</div>

---

## Header Styles

# Header One

## Header Two

### Header Three

#### Header Four

##### Header Five

###### Header Six

# I'm an Header 1 inline flag **Flag**{ .flag } { style='margin: 0' }

## I'm an Header 2 inline flag **Flag**{ .flag } { style='margin: 0' }

### I'm an Header 3 inline flag **Flag**{ .flag } { style='margin: 0' }

---

# Header with Paragraph One

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

## Header with Paragraph Two

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

### Header with Paragraph Three

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

#### Header with Paragraph Four

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

##### Header with Paragraph Five

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

###### Header with Paragraph Six

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida gravida euismod. Aliquam erat volutpat. In at viverra ligula. Ut vitae sollicitudin tortor. Duis varius ultrices augue id feugiat. Morbi sed sapien tellus. Ut gravida ultricies interdum. Nam fermentum, risus et lacinia condimentum, nunc sem convallis sapien, non tempus tortor sem sed purus. Mauris vitae leo tortor. Nulla ac urna elit. Suspendisse mi arcu, placerat ut dui at, convallis dapibus diam. Cras libero purus, commodo quis libero a, fermentum consectetur ante.

---