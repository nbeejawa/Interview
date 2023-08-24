{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "23887caa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing hello.py\n"
     ]
    }
   ],
   "source": [
    "%%file hello.py\n",
    "print \"hello, world!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2a7477d7",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;241;43m1\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m2\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "1 + \"2\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f85d2b14",
   "metadata": {},
   "source": [
    "4/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "45a5a55d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "4/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "122ba0f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.5"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5/2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
