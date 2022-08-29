# (WIP) CSSTOJS

An personal exercise in C, for an application that converts _some_ CSS into the JS CSS styling for React.
This project is very basic and doesn't yet do much.

### The Idea

To convert CSS in the following form when specified an identifier such as `.some-class` or `#some-id`

```css
.some-class {
	font-size: 14px;
	display: flex;
}
#some-id {
	mix-blend-mode: luminosity;
}
```

into a copy-paste format for a very basic JS-in-CSS for React such as:

```JSS
someClass: {
    fontSize: "14px",
    display: "flex",
}
```

for `.some-class` and

```JSS
someId: {
    mixBlendMode: "luminosity",
}
```

for `#some-id` respectively.
