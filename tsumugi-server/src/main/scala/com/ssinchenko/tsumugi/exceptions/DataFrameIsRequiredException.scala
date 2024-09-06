package com.ssinchenko.tsumugi.exceptions

// inspired by https://stackoverflow.com/a/38243657
final case class DataFrameIsRequiredException(
    private val message: String = "",
    private val cause: Throwable = None.orNull
) extends Exception(message, cause)
