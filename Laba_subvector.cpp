#include <iostream>
#include <random>
#include <chrono>

struct subvector {
    int* mas;
    unsigned int top;
    unsigned int capacity;
};

bool init(subvector* qv);
bool push_back(subvector* qv, int d);
int pop_back(subvector* qv);
bool resize(subvector* qv, unsigned int new_capacity);
void shrink_to_fit(subvector* qv);
void clear(subvector* qv);
void destructor(subvector* qv);

// инициализация пустого недовектора (top и capacity по нулям, а mas это NULL)
bool init(subvector* qv)
{
    qv->mas = nullptr;  
    qv->top = 0u;       
    qv->capacity = 0u;  

    return true;        
}
// добавление элемента в конец недовектора с выделением дополнительной памяти при необходимости
bool push_back(subvector* qv, int d)
{
    if (qv->capacity == 0u) {
        resize(qv, 4u);
    }
    else if (qv->top == qv->capacity) {
        resize(qv, qv->capacity * 2u + 4u);
    }
    qv->mas[qv->top] = d;  
    qv->top++;             

    return true;        
}
// удаление элемента с конца недовектора, значение удаленного элемента вернуть (если недовектор пустой, вернуть ноль)
int pop_back(subvector* qv)
{
    if (qv->top == 0u)
        return 0;  
    qv->top--;             
    int value = qv->mas[qv->top];  
    return value;          
}
bool resize(subvector* qv, unsigned int new_capacity)
{
    unsigned int const new_top = (qv->top > new_capacity)
        ? new_capacity    
        : qv->top;        
    int* new_mas = new int[new_capacity];
    for (unsigned int i = 0u; i < new_top; ++i)
    {
        new_mas[i] = qv->mas[i];
    }
    delete[] qv->mas;
    qv->mas = new_mas;       
    qv->top = new_top;   
    qv->capacity = new_capacity;

    return true; 
}

// очистить неиспользуемую память, переехав на новое место с уменьшением capacity до top
void shrink_to_fit(subvector* qv)
{
    resize(qv, qv->top);
}

// очистить содержимое недовектора, занимаемое место при этом не меняется
void clear(subvector* qv)
{
    qv->top = 0u;
}

// очистить всю используемую память, инициализировать недовектор как пустой
void destructor(subvector* qv)
{
    delete[] qv->mas;  
    init(qv);          
}