#!/usr/bin/env python
# coding=utf-8
import random

init_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz'

def generate(size):
    return ''.join(random.choice(init_chars) for _ in range(size))


