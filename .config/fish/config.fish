if status is-interactive
    # Commands to run in interactive sessions can go here
    set fish_greeting
    neofetch --colors 3 5 5 3 3 7
    starship init fish | source
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
end
