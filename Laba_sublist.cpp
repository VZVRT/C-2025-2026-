struct subforwardlist {
    int data;
    subforwardlist* next;
};

bool init(subforwardlist** sfl) {
    *sfl = nullptr;
    return true;
}; //инициализация пустого недосписка

bool push_back(subforwardlist** sfl, int d) {
    subforwardlist* tmp = *sfl;

    subforwardlist* last = new subforwardlist;
    last->data = d;
    last->next = nullptr;

    if (*sfl == nullptr) {
        *sfl = last;
        return true;
    }

    while (tmp->next) {
        tmp = tmp->next;
    }

    tmp->next = last;
    return true;
}; //добавление элемента в конец недосписка

int pop_back(subforwardlist** sfl) {
    if (*sfl == nullptr) return 0;

    if ((*sfl)->next == nullptr) {
        int d = (*sfl)->data;
        delete (*sfl);
        *sfl = nullptr;
        return d;
    }

    subforwardlist* tmp = *sfl;

    while (tmp->next->next) {
        tmp = tmp->next;
    }

    int d = tmp->next->data;
    delete tmp->next;
    tmp->next = nullptr;

    return d;
}; //удаление элемента с конца недосписка, если пустой - возвращать 0

bool push_forward(subforwardlist** sfl, int d) {
    subforwardlist* tmp = new subforwardlist;
    tmp->data = d;
    tmp->next = *sfl;
    *sfl = tmp;
    return true;
}; //добавление элемента в начало недосписка

int pop_forward(subforwardlist** sfl) {
    if (*sfl == nullptr) return 0;

    int d = (*sfl)->data;
    subforwardlist* sec = (*sfl)->next;
    delete (*sfl);
    *sfl = sec;
    return d;
}; //удаление элемента из начала недосписка, если пустой - возвращать 0

bool push_where(subforwardlist** sfl, unsigned int where, int d) {
    subforwardlist* tmp = *sfl;
    subforwardlist* cur = new subforwardlist;
    cur->data = d;
    cur->next = nullptr;

    if (*sfl == nullptr) {
        *sfl = cur;
        return true;
    }

    if (where == 0) {
        cur->next = *sfl;
        *sfl = cur;
        return true;
    }

    for (unsigned int i = 0; i < where - 1; ++i) {
        if (tmp->next == nullptr) {
            delete cur;
            return false;
        }
        tmp = tmp->next;
    }

    cur->next = tmp->next;
    tmp->next = cur;
    return true;
}; //добавление элемента с порядковым номером where

int erase_where(subforwardlist** sfl, unsigned int where) {
    if (*sfl == nullptr) return 0;

    if (where == 0) {
        return pop_forward(sfl);
    }

    subforwardlist* tmp = *sfl;

    for (unsigned int i = 0; i < where - 1; ++i) {
        if (tmp->next == nullptr) {
            return 0;
        }
        tmp = tmp->next;
    }

    if (tmp->next == nullptr) {
        return 0;
    }

    subforwardlist* to_delete = tmp->next;
    int d = to_delete->data;
    tmp->next = to_delete->next;
    delete to_delete;
    return d;
}; //удаление элемента с порядковым номером where, если пустой - возвращать 0

unsigned int size(subforwardlist** sfl) {
    subforwardlist* tmp = *sfl;
    unsigned int cnt = 0;

    while (tmp) {
        cnt++;
        tmp = tmp->next;
    }
    return cnt;
}; //определить размер недосписка

void clear(subforwardlist** sfl) {
    while (*sfl) {
        pop_forward(sfl);
    }
}; //очистить содержимое недосписка

