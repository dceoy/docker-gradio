#!/usr/bin/env python

import argparse

import gradio as gr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='User')
    args, _ = parser.parse_known_args()

    with gr.Blocks() as demo:
        gr.Markdown(f'# Greetings {args.name}!')
        inp = gr.Textbox()
        out = gr.Textbox()
        inp.change(fn=lambda x: x, inputs=inp, outputs=out)

    demo.launch()
