
trieNode = {
    "children": {},
    "is_end_of_word": False
}

words = ["cat", "banana", "obama", "car", "cow", "alibaba", "bana"]

children = {
    "c": {
        "children": {
            "a": {
                "children": {
                    "t": {
                        "children": {},
                        "is_end_of_word": True
                    },
                    "r": {
                        "children": {},
                        "is_end_of_word": True
                    }
                },
                "is_end_of_word": False
            },
            "o": {
                "children": {
                    "w": {
                        "children": {},
                        "is_end_of_word": True
                    }    
                },
                "is_end_of_word": False
            }
        },
        "is_end_of_word": False
    },
    "b": {
        "children": {
            "a": {
                "children": {
                    "n": {
                        "children": {
                            "a": {
                                "children": {
                                    "n": {
                                        "children": {
                                            "a": {
                                                "children": {},
                                                "is_end_of_word": True
                                            }    
                                        },
                                        "is_end_of_word": False
                                    }    
                                },
                                "is_end_of_word": True
                            }
                        }
                    },
                    "is_end_of_word": False
                }
            },
            "is_end_of_word": False
        },
        "is_end_of_word": False
    },
    "o": {
        "children": {
            "b": {
                "children": {
                    "a": {
                        "children": {
                            "m": {
                                "children": {
                                    "a": {
                                        "children": {},
                                        "is_end_of_word": True
                                    }
                                },
                                "is_end_of_word": False
                            }
                        },
                        "is_end_of_word": False
                    }
                },
                "is_end_of_word": False
            }
        },
        "is_end_of_word": False
    },
    "a": {
        "children": {
            "l": {
                "children": {
                    "i": {
                        "children": {
                            "b": {
                                "children": {
                                    "a": {
                                        "children": {
                                            "b": {
                                                "children": {
                                                    "a": {
                                                        "children": {},
                                                        "is_end_of_word": True
                                                    }    
                                                },
                                                "is_end_of_word": False
                                            }    
                                        },
                                        "is_end_of_word": False
                                    }    
                                },
                                "is_end_of_word": False
                            }    
                        },
                        "is_end_of_word": False
                    }
                },
                "is_end_of_word": False
            }    
        },
        "is_end_of_word": False
    }
    
}


root = {
    "children": {
        "c": {
            "children": {"a"},
            "endWord": False
        }
    },
    "endWord": False
}